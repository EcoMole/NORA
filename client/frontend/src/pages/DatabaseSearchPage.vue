<template>
  <div>
    <h1>Database Search</h1>
  </div>
  <DatabaseSearchFilters
    v-if="showFilterInterface"
    :selectedAttrsFromPreviousSearch="selectedAttrs"
    :addedFiltersFromPreviousSearch="addedFilters"
    @render-table="renderTable"
    @close="showFilterInterface = false"
  />
  <v-row v-else>
    <v-sheet elevation="2" class="mt-2 pa-4" style="overflow-x: auto; width: 100%">
      <!-- v-slot is a directive in Vue.js that allows you to define a slot in a component. Slots are placeholders that you can fill with content when using the component. When using v-slot, you are essentially injecting custom content into a specific part of a child component. -->
      <!-- The { item } represents the entire object (row) for the current item in the table. -->

      <v-skeleton-loader
        v-if="!fetchedNovelFoods"
        class="mx-auto"
        type="table-thead, table-tbody, table-tbody, table-tbody"
        style="z-index: 0"
      ></v-skeleton-loader>
      <!-- opinion, id, __typename -->
      <v-data-table
        v-if="fetchedNovelFoods"
        :headers="createHeaders(fetchedNovelFoods[0])"
        :items="fetchedNovelFoods"
        style="font-size: 12px"
        density="compact"
        :loading="tableIsLoading"
      >
        <!-- slot creation for opinion, id, __typename -->
        <template
          v-for="(key, index) in Object.keys(fetchedNovelFoods[0])"
          v-slot:[`item.${key}`]="{ item }"
          :key="`1-${index}`"
        >
          <div>
            <template v-if="createNestedTable(item[key])">
              <!-- table inside Opinion table -->
              <!-- documentType, title, doi, url, atd. -->
              <!-- key here is Opinion a item[key] is content of Opinion column -->
              <!-- content of opinion is allways object -->
              <v-data-table
                :headers="createHeaders(Array.isArray(item[key]) ? item[key][0] : item[key])"
                :items="Array.isArray(item[key]) ? item[key] : [item[key]]"
                style="font-size: 10px"
                density="compact"
                hide-default-footer
              >
                <!-- column creation documentType, doi, url -->
                <!-- next level -->
                <template
                  v-for="(key, index) in Object.keys(
                    Array.isArray(item[key]) ? item[key][0] : item[key]
                  )"
                  v-slot:[`item.${key}`]="{ item }"
                  :key="`2-${index}`"
                >
                  <div>
                    <template v-if="createNestedTable(item[key])">
                      <v-data-table
                        :headers="
                          createHeaders(Array.isArray(item[key]) ? item[key][0] : item[key])
                        "
                        :items="Array.isArray(item[key]) ? item[key] : [item[key]]"
                        style="font-size: 10px"
                        density="compact"
                        hide-default-footer
                      >
                        <!-- next level -->
                        <template
                          v-for="(key, index) in Object.keys(
                            Array.isArray(item[key]) ? item[key][0] : item[key]
                          )"
                          v-slot:[`item.${key}`]="{ item }"
                          :key="`3-${index}`"
                        >
                          <div>
                            <template v-if="createNestedTable(item[key])">
                              <v-data-table
                                :headers="
                                  createHeaders(Array.isArray(item[key]) ? item[key][0] : item[key])
                                "
                                :items="Array.isArray(item[key]) ? item[key] : [item[key]]"
                                style="font-size: 10px"
                                density="compact"
                                hide-default-footer
                              >
                                <!-- next level -->
                                <template
                                  v-for="(key, index) in Object.keys(
                                    Array.isArray(item[key]) ? item[key][0] : item[key]
                                  )"
                                  v-slot:[`item.${key}`]="{ item }"
                                  :key="`4-${index}`"
                                >
                                  <div>
                                    <template v-if="createNestedTable(item[key])">
                                      <v-data-table
                                        :headers="
                                          createHeaders(
                                            Array.isArray(item[key]) ? item[key][0] : item[key]
                                          )
                                        "
                                        :items="Array.isArray(item[key]) ? item[key] : [item[key]]"
                                        style="font-size: 10px"
                                        density="compact"
                                        hide-default-footer
                                      >
                                      </v-data-table>
                                    </template>
                                    <template v-else> {{ item[key] }} </template>
                                  </div>
                                </template>
                              </v-data-table>
                            </template>
                            <template v-else> {{ item[key] }} </template>
                          </div>
                        </template>
                      </v-data-table>
                    </template>
                    <template v-else> {{ item[key] }} </template>
                  </div>
                </template>
              </v-data-table>
            </template>
            <template v-else> {{ item[key] }}</template>
          </div>
        </template>
      </v-data-table>
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
        <v-list-item v-for="(option, i) in exportOptions" :key="i" :value="i">
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
</template>

<script>
import { useTheme } from 'vuetify'
import DatabaseSearchFilters from '@/components/DatabaseSearchFilters.vue'
import { buildQraphQLQuery } from '@/libs/graphql-query.js'
import { useMainStore } from '@/stores/main'
// import { buildQraphQLQuery } from '@/libs/graphql-query'
// for Composition API apollo provider:
// import { useApolloClient } from '@vue/apollo-composable'
// icon: 'mdi-rice'
// icon: 'mdi-alert-outline'
// icon: 'mdi-hazard-lights'
// icon: 'mdi-shield-alert'

export default {
  components: { DatabaseSearchFilters },
  data: () => ({
    tableIsLoading: false,
    exportOptions: [
      { title: 'the search result', icon: 'mdi-table' },
      { title: 'the whole database', icon: 'mdi-database' }
    ],
    showFilterInterface: true,
    headers: [],
    fetchedNovelFoods: null,
    addedFilters: [],
    selectedAttrs: []
  }),
  methods: {
    buildQraphQLQuery: buildQraphQLQuery,
    async renderTable(addedFilters, selectedAttrs) {
      this.addedFilters = addedFilters
      this.selectedAttrs = selectedAttrs
      this.tableIsLoading = true
      const QUERY = this.buildQraphQLQuery(this.selectedAttrs)
      const nfTitle = this.addedFilters.filter((filter) => filter.title === 'novel food title')[0]
        ?.value

      try {
        // using this.$apollo for Option API apollo provider
        // for Composition API apollo provider use: const { client } = useApolloClient()
        const response = await this.$apollo.query({
          query: QUERY,
          variables: {
            novelFoodTitle: nfTitle
          }
        })
        this.fetchedNovelFoods = response.data.novelFoods
        console.log(this.fetchedNovelFoods)
      } catch (error) {
        this.mainStore.handleError(error['message'])
      } finally {
        this.tableIsLoading = false
      }
    },
    createNestedTable(param) {
      return (
        param != null &&
        ((param.constructor === Object && Object.keys(param).length > 0) ||
          (Array.isArray(param) && param.length > 0))
      )
    },

    createHeaders(object) {
      const headers = Object.keys(object)
        .filter((key) => key !== '__typename' && key !== 'id') // Exclude specific keys
        .map((key) => ({
          title: key,
          value: key,
          align: 'center'
        }))

      return headers
    },

    newSearch() {
      this.showFilterInterface = true
      this.addedFilters = []
      this.selectedAttrs = []
    }
  },
  created() {
    this.theme = useTheme()
    this.mainStore = useMainStore()
  }
}
</script>

<style>
th {
  color: #557c55;
}
</style>
