<template>
  <div>
    <!-- {{this.fetchedNovelFoods || ""}} -->
  </div>
  <div>
    <h1>Database Search</h1>
    <DatabaseSearchFilters
      v-if="showFilterInterface"
      :selectedFieldsFromPreviousSearch="selectedFields"
      :addedFiltersFromPreviousSearch="addedFilters"
      @render-table="renderTable"
      @close="showFilterInterface = false"
    />
    <v-row v-else>
      <v-sheet elevation="2" class="mt-2 pa-4" style="overflow-x: auto; width: 100%">
        <v-skeleton-loader
          v-if="!fetchedNovelFoods"
          class="mx-auto"
          type="table-thead, table-tbody, table-tbody, table-tbody"
          style="z-index: 0"
        ></v-skeleton-loader>
        <div v-else>
          <RecursiveDataTable
            :data="fetchedNovelFoods.map((edge) => edge.node)"
            :loading="tableIsLoading"
            :nameMappingObj="nameMappingObj"
            :headdersToHide="headdersToHide"
          />
        </div>
      </v-sheet>

      <!-- btns -->
      <v-menu :rounded="'lg'">
        <template v-slot:activator="{ props: menuProps }">
          <v-hover v-slot="{ isHovering, props: hoverProps }">
            <v-btn
              v-bind="{ ...hoverProps, ...menuProps }"
              :elevation="isHovering ? 14 : 4"
              size="small"
              min-height="40px"
              color="primary"
              style="margin-top: 98px"
              position="fixed"
              location="top right"
              class="mr-10"
              :ripple="false"
            >
              <v-icon left>mdi-download</v-icon>
              Export
            </v-btn>
          </v-hover>
        </template>
        <v-list density="compact">
          <v-list-item v-for="(option, i) in exportOptions" :key="i" :value="i" @click="handleExport(i)">
            <template v-slot:prepend>
              <v-icon :icon="option.icon"></v-icon>

            </template>
            <v-list-item-title>{{ option.title }}</v-list-item-title>
          </v-list-item>
        </v-list>
      </v-menu>
      <v-hover v-slot="{ isHovering, props }">
        <v-btn
          v-bind="props"
          :elevation="isHovering ? 14 : 4"
          @click="newSearch"
          size="small"
          min-height="50px"
          color="tertiary"
          style="margin-bottom: 98px"
          position="fixed"
          location="bottom right"
          class="mr-10"
          :ripple="false"
        >
          <v-icon left>mdi-replay</v-icon>
          new search
        </v-btn>
      </v-hover>
      <!-- grouped repeated switch -->
      <!-- <v-sheet
      elevation="24"
      position="fixed"
      location="bottom"
      class="mb-8 px-5"
      rounded="lg"
      border
    >
      <v-row class="d-flex align-center">
        <v-col class="text-right">
          <label
            for="custom-switch"
            :style="{ fontWeight: tableStyle == grouped ? 'bold' : 'normal' }"
            >{{ grouped }}
            <v-tooltip activator="parent" location="left"
              >Shows a single value for all rows that share the same value.</v-tooltip
            ></label
          >
        </v-col>

        <v-col>
          <v-switch
            density="compact"
            v-model="tableStyle"
            id="custom-switch"
            hide-details
            :false-value="grouped"
            :true-value="repeated"
          ></v-switch>
        </v-col>

        <v-col>
          <label
            for="custom-switch"
            :style="{ fontWeight: tableStyle == repeated ? 'bold' : 'normal' }"
          >
            {{ repeated }}
            <v-tooltip activator="parent" location="right"
              >Repeats each value for all rows that share the same value.</v-tooltip
            ></label
          >
        </v-col>
      </v-row>
    </v-sheet> -->
      <v-btn
        elevation="24"
        @click="showFilterInterface = true"
        min-height="50px"
        color="secondary"
        position="fixed"
        location="bottom right"
        class="mb-8 mr-10"
        :ripple="false"
      >
        <v-icon left>mdi-replay</v-icon>
        edit search
      </v-btn>
    </v-row>
  </div>
</template>

<script>
import { useTheme } from 'vuetify'
import DatabaseSearchFilters from '@/components/DatabaseSearchFilters.vue'
import { buildQueryFromSelectedFields } from '@/libs/graphql-query.js'
import { useMainStore } from '@/stores/main'
import RecursiveDataTable from '@/components/RecursiveDataTable.vue'
import { objectTypes, fields } from '@/libs/definitions.js'
import { buildVariables } from '@/libs/utils.js'
import axios from '@/libs/axios'

export default {
  components: { DatabaseSearchFilters, RecursiveDataTable },
  data: () => ({
    tableIsLoading: false,
    exportOptions: [
      { title: 'the search result', icon: 'mdi-table' },
      //{ title: 'the whole database', icon: 'mdi-database' }
    ],
    showFilterInterface: true,
    fetchedNovelFoods: null,
    addedFilters: [],
    selectedFields: {},
    headdersToHide: [],
    nameMappingObj: { ...objectTypes, ...fields }
  }),
  methods: {
    buildQueryFromSelectedFields: buildQueryFromSelectedFields,
    buildVariables: buildVariables,
    async renderTable(addedFilters, selectedFields, headdersToHide) {
      this.headdersToHide = headdersToHide
      this.addedFilters = addedFilters
      this.selectedFields = selectedFields
      this.tableIsLoading = true
      const variables = buildVariables(this.addedFilters)
      const QUERY = this.buildQueryFromSelectedFields(variables, this.selectedFields)
      try {
        // using this.$apollo for Option API apollo provider
        // for Composition API apollo provider use: const { client } = useApolloClient()
        const response = await this.$apollo.query({
          query: QUERY,
          variables: variables
        })
        this.fetchedNovelFoods = response.data.novelFoods.edges
        /* console.log('this.fetchedNovelFoods', this.fetchedNovelFoods) */
      } catch (error) {
        this.mainStore.handleError(error['message'])
      } finally {
        this.tableIsLoading = false
      }
    },
    newSearch() {
      this.showFilterInterface = true
      this.addedFilters = []
      this.selectedFields = []
    },
    exportSearchResult() {
      console.log('exporting search result')
      axios.post('/api/v1/export/', this.fetchedNovelFoods, {responseType: 'blob'})
      .then(response => {
      // Handle success (e.g., trigger download if needed)
      console.log('Export successful', response);
      const blob = new Blob([response.data], { type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet' });
    
      // Create a download link for the Excel file
      const link = document.createElement('a');
      link.href = URL.createObjectURL(blob);
      link.setAttribute('download', 'exported_data.xlsx');  // Specify the filename
      document.body.appendChild(link);  // Append link to the body
      link.click();  // Programmatically click the link to trigger the download
      document.body.removeChild(link);
      })
      .catch(error => {
        console.error('Error exporting:', error);
      });
    },
    exportWholeDatabase() {
      console.log('exporting whole database')
    },
    handleExport(i) {
      console.log('exporting', i)
      if (i === 0) {
        this.exportSearchResult();
      } else if (i === 1) {
        this.exportWholeDatabase();
      }
    },
  },
  created() {
    this.theme = useTheme()
    this.mainStore = useMainStore()
  }
}
</script>

<style></style>
