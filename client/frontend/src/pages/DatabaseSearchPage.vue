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
            :data="toArray(fetchedNovelFoods)"
            :loading="tableIsLoading"
            :nameMappingObj="nameMappingObj"
            :headdersToHide="headdersToHide"
          />
        </div>
      </v-sheet>

      <!-- btns -->
      <v-hover v-slot="{ isHovering, props: hoverProps }">
        <v-btn
          v-bind="{ ...hoverProps }"
          :elevation="isHovering ? 14 : 4"
          size="small"
          min-height="40px"
          color="primary"
          style="margin-top: 98px"
          position="fixed"
          location="top right"
          class="mr-10"
          :ripple="false"
          @click="exportSearchResult"
          :loading="exporting"
        >
          <v-icon left>mdi-download</v-icon>
          Export
        </v-btn>
      </v-hover>
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
import { buildQueryFromSelectedFields, formatGraphQLQuery } from '@/libs/graphql-query.js'
import { useMainStore } from '@/stores/main'
import RecursiveDataTable from '@/components/RecursiveDataTable.vue'
import { objectTypes, fields } from '@/libs/definitions.js'
import { buildVariables } from '@/libs/utils.js'
import axios from '@/libs/axios'

export default {
  components: { DatabaseSearchFilters, RecursiveDataTable },
  data: () => ({
    tableIsLoading: false,
    showFilterInterface: true,
    fetchedNovelFoods: null,
    addedFilters: [],
    selectedFields: {},
    headdersToHide: [],
    nameMappingObj: { ...objectTypes, ...fields },
    exporting: false
  }),
  methods: {
    toArray(value) {
      return Array.isArray(value) ? value : [value]
    },
    buildQueryFromSelectedFields: buildQueryFromSelectedFields,
    formatGraphQLQuery: formatGraphQLQuery,
    buildVariables: buildVariables,
    async renderTable(addedFilters, selectedFields, headdersToHide) {
      this.headdersToHide = headdersToHide
      this.addedFilters = addedFilters
      this.selectedFields = selectedFields
      this.tableIsLoading = true
      console.log('this.addedFilters', this.addedFilters)
      const startTime = performance.now()
      const query = this.formatGraphQLQuery(selectedFields)
      const filters = buildVariables(this.addedFilters)
      console.log('filters', filters)
      console.log('query', query)
      try {
        const response = await this.$apollo.query({
          query: query,
          variables: {
            filters: filters
          },
          fetchPolicy: 'network-only' // Ensures that the cache is bypassed and data is fetched from the network
        })
        this.fetchedNovelFoods = response.data.novelFoods.edges.map((edge) => edge.node)
        console.log('this.fetchedNovelFoods', this.fetchedNovelFoods)
      } catch (error) {
        this.mainStore.handleError(error['message'])
      } finally {
        const endTime = performance.now()
        const timeTaken = endTime - startTime
        console.log(`Query and processing took ${timeTaken.toFixed(2)} milliseconds.`)
        this.tableIsLoading = false
      }
    },
    newSearch() {
      this.showFilterInterface = true
      this.addedFilters = []
      this.selectedFields = []
    },
    exportSearchResult() {
      this.exporting = true
      console.log('exporting search result')
      axios
        .post('/api/v1/export/', this.fetchedNovelFoods, { responseType: 'blob' })
        .then((response) => {
          // Handle success (e.g., trigger download if needed)
          console.log('Export successful', response)
          const blob = new Blob([response.data], {
            type: 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
          })

          // Create a download link for the Excel file
          const link = document.createElement('a')
          link.href = URL.createObjectURL(blob)
          link.setAttribute('download', 'exported_data.xlsx') // Specify the filename
          document.body.appendChild(link) // Append link to the body
          link.click() // Programmatically click the link to trigger the download
          document.body.removeChild(link)
        })
        .catch((error) => {
          console.error('Error exporting:', error)
        })
        .finally(() => {
          this.exporting = false
        })
    }
  },
  created() {
    this.theme = useTheme()
    this.mainStore = useMainStore()
  }
}
</script>

<style></style>
