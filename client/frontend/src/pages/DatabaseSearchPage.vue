<template>
  <div>
    <DatabaseSearchFilters
      v-if="showFilterInterface"
      :selectedFieldsFromPreviousSearch="selectedFields"
      :addedFiltersFromPreviousSearch="addedFilters"
      @render-table="renderTable"
      @close="showFilterInterface = false"
    />
    <v-row v-else>
      <v-sheet elevation="2" class="pa-4" style="overflow-x: auto; width: 100%">
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
            :showCompactTable="showCompactTable"
          />
        </div>
      </v-sheet>

      <!-- btns -->

      <v-hover v-slot="{ isHovering, props }">
        <v-btn
          v-bind="props"
          :elevation="isHovering ? 14 : 4"
          @click="newSearch"
          size="small"
          min-height="50px"
          color="tertiary"
          :style="{ marginBottom: '20px', left: '80px' }"
          position="fixed"
          location="bottom left"
          :ripple="false"
        >
          <v-icon left>mdi-replay</v-icon>
          new search
        </v-btn>
      </v-hover>
      <!-- compact extended table switch -->
      <v-sheet
        v-if="offeringCompactTable"
        elevation="24"
        position="fixed"
        location="bottom"
        class="mb-5 px-5"
        rounded="lg"
      >
        <v-row class="d-flex align-center">
          <v-col class="text-right">
            <label for="custom-switch" :style="{ fontWeight: showCompactTable ? 'normal' : 'bold' }"
              >extended
              <!-- <v-tooltip activator="parent" location="left"
                >all the items will be displayed plainly</v-tooltip
              > -->
            </label>
          </v-col>
          <v-col>
            <v-switch
              density="compact"
              v-model="showCompactTable"
              id="custom-switch"
              hide-details
            ></v-switch>
          </v-col>

          <v-col>
            <label for="custom-switch" :style="{ fontWeight: showCompactTable ? 'bold' : 'normal' }"
              >compact
              <!-- <v-tooltip activator="parent" location="right"
                >if more than 10 items will be displayed in table with pages</v-tooltip
              > -->
            </label>
          </v-col>
        </v-row>
      </v-sheet>
      <v-hover v-slot="{ isHovering, props }">
        <v-btn
          v-bind="props"
          :elevation="isHovering ? 14 : 4"
          size="small"
          min-height="40px"
          color="primary"
          position="fixed"
          location="bottom right"
          :style="{ marginBottom: isAtBottom ? '142px' : '80px', right: '25px' }"
          :ripple="false"
          @click="exportSearchResult"
          :loading="exporting"
        >
          <v-icon left>mdi-download</v-icon>
          Export
        </v-btn>
      </v-hover>
      <v-btn
        elevation="24"
        @click="showFilterInterface = true"
        min-height="50px"
        color="secondary"
        position="fixed"
        location="bottom right"
        :ripple="false"
        :style="{ marginBottom: isAtBottom ? '82px' : '20px', right: '25px' }"
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
import { formatGraphQLQuery } from '@/libs/graphql-query.js'
import { useMainStore } from '@/stores/main'
import RecursiveDataTable from '@/components/RecursiveDataTable.vue'
import { objectTypes, coupledFilterFields, simpleFilterFields } from '@/libs/definitions.js'
import { buildVariables } from '@/libs/utils.js'
import axios from '@/libs/axios'
import { mapState, mapActions } from 'pinia'

export default {
  components: { DatabaseSearchFilters, RecursiveDataTable },
  data: () => ({
    tableIsLoading: false,
    showFilterInterface: true,
    fetchedNovelFoods: null,
    addedFilters: [],
    selectedFields: {},
    headdersToHide: [],
    objectTypes: objectTypes,
    nameMappingObj: { ...simpleFilterFields, ...coupledFilterFields, ...objectTypes },
    exporting: false,
    showCompactTable: false,
    isAtBottom: false
  }),
  computed: {
    ...mapState(useMainStore, ['offeringCompactTable'])
  },
  methods: {
    ...mapActions(useMainStore, ['resetOfferingCompactTable']),
    toArray(value) {
      return Array.isArray(value) ? value : [value]
    },
    checkScroll() {
      // scrollTop: How far the user has scrolled from the top.
      const scrollTop = window.scrollY || document.documentElement.scrollTop

      // windowHeight: The height of the display
      const windowHeight = window.innerHeight

      // documentHeight: The total height of the document's content
      const docHeight = document.documentElement.scrollHeight

      if (windowHeight + scrollTop >= docHeight - 1) {
        this.isAtBottom = true
      } else {
        this.isAtBottom = false
      }
    },
    formatGraphQLQuery: formatGraphQLQuery,
    buildVariables: buildVariables,
    selectedFiltersToText() {
      if (this.addedFilters.length === 0) {
        return ['No filters applied']
      }
      return this.addedFilters.map(({ key, include, coupledFilters }) => {
        let text = `All Novel Foods ${include} ${this.nameMappingObj[key].displayName}`

        if (Object.keys(this.objectTypes).includes(key)) {
          coupledFilters.forEach((cF, index) => {
            if (index !== 0) {
              text += ' and'
            }
            text += ` ${cF.include} ${
              this.nameMappingObj[cF.key].flattenedDisplayName
                ? this.nameMappingObj[cF.key].flattenedDisplayName
                : this.nameMappingObj[cF.key].displayName
            } which ${cF.qualifier} ${cF.value}`
          })
        } else {
          text += ` which ${coupledFilters[0].qualifier} ${coupledFilters[0].value}`
        }
        return text
      })
    },
    async renderTable(addedFilters, selectedFields, headdersToHide) {
      this.resetOfferingCompactTable()
      this.headdersToHide = headdersToHide
      this.addedFilters = addedFilters
      this.selectedFields = selectedFields
      this.tableIsLoading = true
      const query = this.formatGraphQLQuery(selectedFields)
      const filters = buildVariables(this.addedFilters)
      try {
        const response = await this.$apollo.query({
          query: query,
          variables: {
            filters: filters
          }
        })
        this.fetchedNovelFoods = response.data.novelFoods.edges.map((edge) => edge.node)
      } catch (error) {
        this.mainStore.handleError(error['message'])
      } finally {
        this.tableIsLoading = false
      }
    },
    newSearch() {
      this.showFilterInterface = true
      this.addedFilters = []
      this.selectedFields = {}
    },
    exportSearchResult() {
      this.exporting = true
      axios
        .post('/api/v1/export/', [this.fetchedNovelFoods, this.selectedFiltersToText()], {
          responseType: 'blob'
        })
        .then((response) => {
          // Handle success (e.g., trigger download if needed)
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
  },
  mounted() {
    // once user scrolls the checkScroll function will be called
    window.addEventListener('scroll', this.checkScroll)
  },
  beforeUnmount() {
    window.removeEventListener('scroll', this.checkScroll)
  }
}
</script>

<style></style>
