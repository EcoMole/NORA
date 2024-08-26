<template>
  <div>
    <h1>Database Search</h1>
  </div>

  <v-row v-if="showFilterInterface" class="mt-4">
    <v-col cols="7">
      <v-row class="d-flex justify-center">
        <h1 style="color: #a9a9a9">Novel Food Filters</h1>
      </v-row>

      <v-row class="mt-4">
        <v-spacer></v-spacer>
        <v-btn
          v-if="addedFilters.length > 1 ? true : false"
          @click="addedFilters = []"
          color="tertiary"
          size="x-small"
          min-height="30"
          class="mr-6"
          variant="tonal"
        >
          <v-icon left>mdi-close</v-icon>
          all</v-btn
        >
      </v-row>

      <v-row v-if="!addingFilter" class="d-flex justify-center mt-5">
        <v-btn
          color="secondary"
          :variant="addedFilters.length > 0 ? 'tonal' : 'elevated'"
          @click="addingFilter = true"
        >
          <v-icon left>mdi-plus</v-icon>
          Add Filter
        </v-btn>
      </v-row>
      <v-row v-else class="d-flex justify-end mb-0">
        <v-col cols="12" class="mr-1">
          <v-card
            class="pa-2"
            rounded="xl"
            elevation="6"
            density="compact"
            @keyup.enter="addFilter"
          >
            <v-card-subtitle class="text-h6 pt-4">
              {{ this.availableFilters[newFilter.title]?.group || '' }}
            </v-card-subtitle>
            <v-card-text class="pb-0">
              <v-container>
                <v-row>
                  <v-col cols="12">
                    <v-row class="d-flex align-center">
                      <span>All Novel Foods</span>
                      <v-select
                        v-model="newFilter.include"
                        :items="['must have', 'must not have']"
                        class="ml-6"
                        variant="underlined"
                        max-width="140px"
                      ></v-select>
                      <v-autocomplete
                        v-model="newFilter.title"
                        :items="Object.keys(availableFilters)"
                        class="ml-6"
                        variant="underlined"
                        @change="updateSubtitle"
                      ></v-autocomplete>
                    </v-row>
                  </v-col>
                  <v-col cols="12">
                    <v-row class="d-flex align-center">
                      <span v-if="newFilter.title">which</span>
                      <v-autocomplete
                        :disabled="!newFilter.title"
                        v-model="newFilter.qualifier"
                        :items="availableFilters[newFilter.title]?.qualifiers || []"
                        max-width="180px"
                        variant="underlined"
                        class="ml-6"
                      ></v-autocomplete>
                      <v-text-field
                        variant="underlined"
                        v-model="newFilter.value"
                        :type="availableFilters[newFilter.title]?.type"
                        class="ml-6"
                        :disabled="!newFilter.title"
                      ></v-text-field>
                    </v-row>
                  </v-col>

                  <v-col v-if="availableFilters[newFilter.title]?.description" cols="12">
                    <p>
                      {{ availableFilters[newFilter.title]?.description }}
                    </p>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
            <v-card-actions class="mb-1 pt-0">
              <v-spacer></v-spacer>
              <v-btn color="tertiary" variant="tonal" @click="cancelNewFilter">Cancel</v-btn>
              <v-btn
                color="secondary"
                :disabled="!addFilterValid"
                variant="elevated"
                class="mr-2 ml-5"
                @click="addFilter"
                >Save</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
      <v-row v-for="(filter, i) in addedFilters" :key="i" class="mb-0">
        <v-row class="d-flex justify-center mb-0" v-if="i != 0 || addingFilter == true">
          <span class="mt-0">and</span>
        </v-row>
        <v-col cols="12" class="mb-0">
          <v-card class="pa-2 mb-0 mr-1" elevation="3" style="position: relative" rounded="xl">
            <v-btn
              :style="{ position: 'absolute', right: '+8px' }"
              color="tertiary"
              size="x-small"
              min-height="30"
              @click="removeItem(i)"
              variant="tonal"
              style="z-index: 2"
            >
              <v-icon>mdi-close</v-icon>
            </v-btn>

            <v-card-subtitle class="text-h6 pt-3 pb-2 mb-0">
              {{ filter.group }}
            </v-card-subtitle>
            <v-card-text class="pt-0">
              Novel Foods <b>{{ filter.include }}</b> {{ ' ' }}
              <v-chip rounded="pill" density="compact" class="pb-1" color="secondary">{{
                filter.title
              }}</v-chip
              >{{ ' ' }}which <b>{{ filter.qualifier }}</b
              >{{ ' ' }}
              <v-chip rounded="pill" density="compact" class="pb-1" color="secondary">{{
                filter.value
              }}</v-chip>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-col>
    <v-divider :thickness="2" vertical class="ml-0"></v-divider>
    <v-col cols="4">
      <v-row class="d-flex justify-center">
        <h1 style="color: #a9a9a9">Data to be fetched</h1>
      </v-row>
      <v-row class="mt-3">
        <v-container>
          <v-alert
            class="mb-3"
            v-if="selectedAttrs.length < 1"
            icon="$warning"
            text="Select data you would like to see"
            color="secondary"
            rounded="md"
          ></v-alert>
          <v-row v-if="selectedAttrs.length > 1" class="mb-2">
            <v-spacer></v-spacer>
            <v-btn
              @click="selectedAttrs = []"
              color="tertiary"
              size="x-small"
              min-height="30"
              rounded="md"
              variant="tonal"
            >
              <v-icon left>mdi-close</v-icon>
              all
            </v-btn>
          </v-row>
          <v-row class="mt-0">
            <v-col
              v-for="(attr, i) in selectedAttrs"
              :key="attr.text"
              class="py-1 pe-0"
              cols="auto"
            >
              <v-chip
                size="large"
                closable
                elevation="3"
                @click:close="selectedAttrs.splice(i, 1)"
                variant="elevated"
                :color="this.theme.global.current.value.dark ? 'black' : 'white'"
              >
                <v-icon :icon="attr.icon" start></v-icon>

                {{ attr.text }}
              </v-chip>
            </v-col>
          </v-row>
        </v-container>

        <v-container class="mt-4">
          <v-text-field
            v-if="!allSelected"
            v-model="availableAttrsSearch"
            density="comfortable"
            placeholder="Search available data"
            prepend-inner-icon="mdi-magnify"
            style="max-width: 300px"
            variant="outlined"
            clearable
            hide-details
          ></v-text-field>
          <v-list bg-color="rgba(0, 0, 0, 0)" density="compact">
            <template v-for="attr in availableAttrsSearched">
              <v-list-item
                v-if="!selectedAttrs.includes(attr)"
                :key="attr.text"
                @click="selectedAttrs.push(attr)"
              >
                <template v-slot:prepend>
                  <v-icon :icon="attr.icon"></v-icon>
                </template>

                <v-list-item-title>{{ attr.text }}</v-list-item-title>
              </v-list-item>
            </template>
          </v-list>
        </v-container>
      </v-row>
    </v-col>
    <v-btn
      elevation="14"
      :disabled="selectedAttrs.length < 1"
      @click="renderTable"
      style="z-index: 2"
      color="secondary"
      position="fixed"
      location="bottom right"
      class="mb-8 mr-10"
      :ripple="false"
      size="large"
      min-height="50px"
    >
      <v-icon left class="mr-2">mdi-table</v-icon>
      Show data
    </v-btn>
  </v-row>
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
        hide-default-footer
        height="1400px"
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
                :items="[item[key]]"
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
    <v-sheet
      elevation="24"
      position="fixed"
      location="bottom"
      class="mb-8 px-5"
      rounded="lg"
      border
    >
      <v-row class="d-flex align-center">
        <!-- Label for false value -->
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

        <!-- v-switch component -->
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

        <!-- Label for true value -->
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
    </v-sheet>
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
import gql from 'graphql-tag'
// for Composition API apollo provider:
// import { useApolloClient } from '@vue/apollo-composable'
// icon: 'mdi-rice'
// icon: 'mdi-alert-outline'
// icon: 'mdi-hazard-lights'
// icon: 'mdi-shield-alert'

export default {
  data: () => ({
    grouped: 'grouped',
    repeated: 'repeated',
    tableStyle: 'repeated',
    open: ['Users'],
    exportOptions: [
      { title: 'the search result', icon: 'mdi-table' },
      { title: 'the whole database', icon: 'mdi-database' }
    ],
    admins: [
      ['Management', 'mdi-account-multiple-outline'],
      ['Settings', 'mdi-cog-outline']
    ],
    cruds: [
      ['Create', 'mdi-plus-outline'],
      ['Read', 'mdi-file-outline'],
      ['Update', 'mdi-update'],
      ['Delete', 'mdi-delete']
    ],

    fieldOptions: [
      {
        text: 'opinion document type',
        model: 'Opinion',
        field: 'document_type',
        icon: 'mdi-file-document-outline'
      },
      {
        text: 'opinion title',
        model: 'Opinion',
        field: 'title',
        icon: 'mdi-file-document-outline'
      },
      { text: 'opinion doi', model: 'Opinion', field: 'doi', icon: 'mdi-file-document-outline' },
      { text: 'opinion url', model: 'Opinion', field: 'url', icon: 'mdi-file-document-outline' },
      {
        text: 'opinion publication date',
        model: 'Opinion',
        field: 'publication_date',
        icon: 'mdi-file-document-outline'
      },
      {
        text: 'opinion adoption date',
        model: 'Opinion',
        field: 'adoption_date',
        icon: 'mdi-file-document-outline'
      },
      {
        text: "opinion's panel title",
        model: 'Panel',
        field: 'title',
        icon: 'mdi-file-document-outline'
      },
      {
        text: "opinion's scientific officer first name",
        model: 'ScientificOfficer',
        field: 'first_name',
        icon: 'mdi-file-document-outline'
      },
      {
        text: "opinion's scientific officer middle name",
        model: 'ScientificOfficer',
        field: 'middle_name',
        icon: 'mdi-file-document-outline'
      },
      {
        text: "opinion's scientific officer last name",
        model: 'ScientificOfficer',
        field: 'last_name',
        icon: 'mdi-file-document-outline'
      },
      {
        text: 'question number',
        model: 'Question',
        field: 'number',
        icon: 'mdi-file-document-outline'
      },
      {
        text: 'applicant title',
        model: 'Applicant',
        field: 'title',
        icon: 'mdi-file-document-outline'
      },
      {
        text: 'mandate type title',
        model: 'MandateType',
        field: 'title',
        icon: 'mdi-file-document-outline'
      },
      {
        text: 'mandate type definition',
        model: 'MandateType',
        field: 'definition',
        icon: 'mdi-file-document-outline'
      },
      {
        text: 'mandate regulation',
        model: 'Mandate',
        field: 'regulation',
        icon: 'mdi-file-document-outline'
      }
    ],

    availableAttrsSearch: '',
    selectedAttrs: [],
    showFilterInterface: true,
    addingFilter: false,
    headers: [],
    newFilter: {
      include: '',
      title: '',
      group: '',
      qualifier: '',
      value: ''
    },
    availableFilters: {
      'production process': {
        group: 'production process',
        type: 'text',
        qualifiers: ['contains', 'is'],
        description:
          'this is more information and explanation about the production process filter user has just selected. It explains the attribute which will be queried, what values it can hold, etc.'
      },
      'opinion regulation': {
        group: 'administrative',
        type: 'text',
        qualifiers: ['contains', 'is'],
        description:
          'this is more information and explanation about the opinion regulation filter user has just selected. It explains the attribute which will be queried, what values it can hold, etc.'
      },
      'date of publication': {
        group: 'administrative',
        type: 'date',
        qualifiers: ['is', 'greater than', 'less than'],
        description:
          'this is more information and explanation about the date of publication filter user has just selected. It explains the attribute which will be queried, what values it can hold, etc.'
      },
      'type mandate': {
        group: 'administrative',
        type: 'text',
        qualifiers: ['contains', 'is'],
        description:
          'this is more information and explanation about the type mandate filter user has just selected. It explains the attribute which will be queried, what values it can hold, etc.'
      }
    },
    expandedItems: {},

    showIndescriptions: [],
    addedFilters: [],
    fetchedNovelFoods: null
  }),
  methods: {
    getAvailableAttrs() {
      return this.fieldOptions.map((field) => {
        return {
          text: field.text,
          icon: field.icon
        }
      })
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
    async fetchData() {
      try {
        const GET_ALL_DATA = gql`
          query {
            novelFoods {
              id
              opinion {
                id
                documentType {
                  id
                  shortName
                  extendedName
                }
                title
                doi
                url
                publicationDate
                adoptionDate
                panels {
                  id
                  title
                }
                sciOfficers {
                  id
                  firstName
                  middleName
                  lastName
                }
                questions {
                  id
                  number
                  applicants {
                    id
                    title
                  }
                  mandates {
                    id
                    mandateType {
                      id
                      title
                      definition
                    }
                    regulation {
                      id
                      shortName
                      extendedName
                    }
                  }
                }
              }
            }
          }
        `
        // for Composition API apollo provider
        // const { client } = useApolloClient()

        // using this.$apollo for Option API apollo provider
        const result = await this.$apollo.query({
          query: GET_ALL_DATA
        })
        this.fetchedNovelFoods = result.data.novelFoods
        console.log(this.fetchedNovelFoods)
      } catch (err) {
        console.log(err)
      }
    },
    cancelNewFilter() {
      this.addingFilter = false
      this.newFilter = {
        include: '',
        title: '',
        group: '',
        qualifier: '',
        value: ''
      }
    },
    newSearch() {
      this.showFilterInterface = true
      this.addedFilters = []
      this.selectedAttrs = []
    },
    renderTable() {
      this.fetchData()
      this.showFilterInterface = false
    },
    updateSubtitle() {
      const selectedAttribute = this.availableFilters[this.newFilter.title]
      if (selectedAttribute) {
        this.newFilter.group = selectedAttribute.group
      }
    },
    addFilter() {
      if (this.addFilterValid) {
        this.addedFilters.unshift({
          id: this.addedFilters.length + 1,
          include: this.newFilter.include,
          title: this.newFilter.title,
          group: this.availableFilters[this.newFilter.title]?.group || '',
          qualifier: this.newFilter.qualifier,
          value: this.newFilter.value
        })
        this.addingFilter = false
        this.newFilter = {
          include: '',
          title: '',
          group: '',
          qualifier: '',
          value: ''
        }
      }
    },
    removeItem(index) {
      this.addedFilters.splice(index, 1)
    }
  },
  computed: {
    allSelected() {
      const availableAttrs = this.getAvailableAttrs()
      return this.selectedAttrs.length === availableAttrs.length
    },
    addFilterValid() {
      return (
        this.newFilter.include &&
        this.newFilter.title &&
        this.newFilter.qualifier &&
        this.newFilter.value
      )
    },
    availableAttrsSearched() {
      const availableAttrsSearch = this.availableAttrsSearch?.toLowerCase()

      if (!availableAttrsSearch) return this.getAvailableAttrs()

      const availableAttrs = this.getAvailableAttrs()
      return availableAttrs.filter((attr) => {
        const text = attr.text.toLowerCase()

        return text.indexOf(availableAttrsSearch) > -1
      })
    }
  },
  created() {
    this.theme = useTheme()
  }
}
</script>

<style>
th {
  color: #557c55;
}
</style>
