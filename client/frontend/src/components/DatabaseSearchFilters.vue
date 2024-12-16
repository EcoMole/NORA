<template>
  <v-container>
    <v-row class="mt-4">
      <v-col cols="6">
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
                {{ this.newFilter.group }}
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
                          v-model="newFilter.key"
                          :items="filtersItems"
                          item-title="displayName"
                          item-value="key"
                          class="ml-6"
                          variant="underlined"
                          @update:modelValue="updateFilterKey"
                        ></v-autocomplete>
                      </v-row>
                    </v-col>
                    <v-col
                      v-if="
                        Object.keys(coupledFiltersAvailable).length < 1 &&
                        newFilter.coupledFilters.length === 1
                      "
                      cols="12"
                    >
                      <v-row class="d-flex align-center">
                        <v-col cols="12">
                          <v-row class="d-flex align-center">
                            <span>which</span>
                            <v-autocomplete
                              v-model="newFilter.coupledFilters[0].qualifier"
                              :items="allFields[newFilter.coupledFilters[0].key]?.qualifiers || []"
                              max-width="150px"
                              variant="underlined"
                              class="ml-6"
                              :disabled="!newFilter.coupledFilters[0].key"
                            ></v-autocomplete>

                            <v-autocomplete
                              v-if="
                                newFilter.coupledFilters[0].options.length > 0 &&
                                newFilter.coupledFilters[0].qualifier !== 'is None'
                              "
                              v-model="newFilter.coupledFilters[0].value"
                              :items="newFilter.coupledFilters[0].options"
                              variant="underlined"
                              class="ml-6"
                              :disabled="!newFilter.coupledFilters[0].key"
                            ></v-autocomplete>
                            <v-text-field
                              v-if="
                                newFilter.coupledFilters[0].options.length < 1 &&
                                newFilter.coupledFilters[0].qualifier !== 'is None'
                              "
                              variant="underlined"
                              v-model="newFilter.coupledFilters[0].value"
                              :type="allFields[newFilter.coupledFilters[0].key]?.type"
                              class="ml-6"
                              :disabled="!newFilter.coupledFilters[0].key"
                            ></v-text-field>
                          </v-row>
                        </v-col>
                      </v-row>
                    </v-col>
                    <v-col v-else cols="12">
                      <v-row
                        v-for="(coupledFilter, i) in newFilter.coupledFilters"
                        :key="i"
                        class="d-flex align-center"
                      >
                        <v-col v-if="i !== 0" cols="12">
                          <v-row class="d-flex justify-center my-1" v-if="true">
                            <span class="mt-0">and</span>
                          </v-row>
                        </v-col>

                        <v-col cols="1">
                          <v-row class="d-flex align-center">
                            <span>with</span>
                          </v-row>
                        </v-col>
                        <v-col cols="11">
                          <v-card class="pa-2" elevation="4" rounded="lg" density="compact">
                            <v-card-text>
                              <v-col cols="12">
                                <v-row class="d-flex align-center">
                                  <v-autocomplete
                                    v-model="newFilter.coupledFilters[i].key"
                                    :items="coupledFiltersItems"
                                    item-title="displayName"
                                    item-value="key"
                                    class="ml-6"
                                    variant="underlined"
                                    @update:modelValue="updateCoupledFilterKey(i)"
                                  ></v-autocomplete>
                                </v-row>
                              </v-col>
                              <v-col cols="12">
                                <v-row class="d-flex align-center">
                                  <span>which</span>
                                  <v-autocomplete
                                    v-model="newFilter.coupledFilters[i].qualifier"
                                    :items="
                                      allFields[newFilter.coupledFilters[i].key]?.qualifiers || []
                                    "
                                    max-width="150px"
                                    variant="underlined"
                                    class="ml-6"
                                    :disabled="!newFilter.coupledFilters[i].key"
                                  ></v-autocomplete>

                                  <v-autocomplete
                                    v-if="
                                      newFilter.coupledFilters[i].options.length > 0 &&
                                      newFilter.coupledFilters[i].qualifier !== 'is None'
                                    "
                                    v-model="newFilter.coupledFilters[i].value"
                                    :items="newFilter.coupledFilters[i].options"
                                    variant="underlined"
                                    class="ml-6"
                                    :disabled="!newFilter.coupledFilters[i].key"
                                  ></v-autocomplete>
                                  <v-text-field
                                    v-if="
                                      newFilter.coupledFilters[i].options.length < 1 &&
                                      newFilter.coupledFilters[i].qualifier !== 'is None'
                                    "
                                    variant="underlined"
                                    v-model="newFilter.coupledFilters[i].value"
                                    :type="allFields[newFilter.coupledFilters[i].key]?.type"
                                    class="ml-6"
                                    :disabled="!newFilter.coupledFilters[i].key"
                                  ></v-text-field>
                                </v-row>
                              </v-col>
                            </v-card-text>
                            <v-card-actions
                              v-if="newFilter.coupledFilters.length > 1"
                              class="mb-1 pt-0"
                            >
                              <v-spacer></v-spacer>
                              <v-btn
                                color="black"
                                size="small"
                                variant="tonal"
                                @click="newFilter.coupledFilters.splice(i, 1)"
                                >discard</v-btn
                              >
                            </v-card-actions>
                          </v-card>
                        </v-col>
                      </v-row>
                    </v-col>
                  </v-row>
                  <v-row
                    v-if="Object.keys(coupledFiltersAvailable).length > 0"
                    class="d-flex justify-center mt-5"
                  >
                    <v-btn color="secondary" variant="tonal" @click="addCoupledFilter"> and </v-btn>
                  </v-row>
                </v-container>
              </v-card-text>
              <v-card-actions class="mb-1 pt-0">
                <v-spacer></v-spacer>
                <v-btn color="tertiary" variant="tonal" @click="cancelNewFilter">Discard</v-btn>
                <v-btn
                  color="secondary"
                  :disabled="!allFiltersValid"
                  variant="elevated"
                  class="mr-2 ml-5"
                  @click="addFilter"
                  >Save</v-btn
                >
              </v-card-actions>
            </v-card>
          </v-col>
        </v-row>
        <v-row v-for="(filter, fI) in addedFilters" :key="fI" class="mb-0">
          <v-row class="d-flex justify-center mb-0" v-if="fI != 0 || addingFilter == true">
            <span class="mt-0">and</span>
          </v-row>
          <v-col cols="12" class="mb-0">
            <v-card class="pa-2 mb-0 mr-1" elevation="3" style="position: relative" rounded="xl">
              <v-btn
                :style="{ position: 'absolute', right: '+8px' }"
                color="tertiary"
                size="x-small"
                min-height="30"
                @click="removeFilter(fI)"
                variant="tonal"
                style="z-index: 2"
              >
                <v-icon>mdi-close</v-icon>
              </v-btn>
              <v-btn
                :style="{ position: 'absolute', right: '+50px' }"
                color="secondary"
                size="x-small"
                min-height="30"
                @click="editFilter(fI)"
                variant="tonal"
                style="z-index: 2"
              >
                edit
              </v-btn>
              <v-card-subtitle class="text-h6 pt-3 pb-2 mb-0">
                {{ filter.group }}
              </v-card-subtitle>
              <v-card-text v-if="Object.keys(objectTypes).includes(filter.key)" class="pt-0">
                <div class="mb-3">
                  Novel Foods <b>{{ filter.include }}</b> {{ ' ' }}
                  <v-chip rounded="pill" class="pb-1" color="secondary">{{
                    this.objectTypes[filter.key].displayName
                  }}</v-chip>
                </div>
                <div v-for="(coupledFiler, cfI) in filter.coupledFilters" :key="cfI">
                  <span v-if="cfI !== 0">and{{ ' ' }}</span>
                  <span>with{{ ' ' }}</span>
                  <v-chip rounded="pill" density="compact" class="pb-1" color="secondary">{{
                    this.coupledFilterFields[coupledFiler.key].flattenedDisplayName
                      ? this.coupledFilterFields[coupledFiler.key].flattenedDisplayName
                      : this.coupledFilterFields[coupledFiler.key].displayName
                  }}</v-chip
                  >{{ ' ' }}which{{ ' ' }}<b>{{ coupledFiler.qualifier }}</b
                  >{{ ' ' }}
                  <span v-if="coupledFiler.value">"{{ coupledFiler.value }}"</span>
                </div>
              </v-card-text>
              <v-card-text v-else class="pt-0">
                Novel Foods <b>{{ filter.include }}</b> {{ ' ' }}
                <v-chip rounded="pill" class="pb-1" color="secondary">{{
                  this.simpleFilterFields[filter.key].displayName
                }}</v-chip
                >{{ ' ' }}which{{ ' ' }}<b>{{ filter.coupledFilters[0].qualifier }}</b
                >{{ ' ' }}
                <span v-if="filter.coupledFilters[0].value"
                  >"{{ filter.coupledFilters[0].value }}"</span
                >
              </v-card-text>
            </v-card>
          </v-col>
        </v-row>
      </v-col>
      <v-divider :thickness="2" vertical class="ml-0"></v-divider>
      <v-col cols="5">
        <v-row class="d-flex justify-center">
          <h1 style="color: #a9a9a9">Data to be fetched</h1>
        </v-row>
        <v-row class="mt-3">
          <v-container>
            <v-row v-if="alertText">
              <v-alert
                class="mb-3"
                icon="$warning"
                :text="alertText"
                color="secondary"
                rounded="md"
              ></v-alert>
            </v-row>
            <v-row v-if="Object.keys(selectedFields).length > 1" class="mb-2">
              <v-spacer></v-spacer>
              <v-btn
                @click="selectedFields = {}"
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
              <template v-for="(field, key) in selectedFields" :key="key">
                <v-col class="py-1 pe-0" cols="auto">
                  <v-chip
                    class="wrap-text-in-chip"
                    size="large"
                    closable
                    elevation="3"
                    @click:close="delete selectedFields[key]"
                    variant="elevated"
                    :color="theme.global.current.value.dark ? 'black' : 'white'"
                  >
                    <v-icon :icon="field.icon" start></v-icon>
                    {{ field.flattenedDisplayName || field.displayName }}
                  </v-chip>
                </v-col>
              </template>
            </v-row>
          </v-container>

          <v-container class="mt-4">
            <v-row>
              <v-text-field
                v-if="!allFieldsSelected"
                v-model="fieldsSearch"
                density="comfortable"
                placeholder="Search available data"
                prepend-inner-icon="mdi-magnify"
                style="max-width: 300px"
                variant="outlined"
                clearable
                hide-details
              ></v-text-field>
              <v-btn
                v-if="!allFieldsSelected"
                @click="selectedFields = allFields"
                color="secondary"
                size="x-small"
                min-height="30"
                rounded="md"
                variant="tonal"
                class="ml-2 mt-2"
              >
                select <br />
                all
              </v-btn>
            </v-row>
            <v-list bg-color="rgba(0, 0, 0, 0)" density="compact">
              <template v-for="(field, key) in fieldsSearched" :key="key">
                <v-list-item v-show="!(key in selectedFields)" @click="handleClick(field, key)">
                  <template v-slot:prepend>
                    <v-icon :icon="field.icon"></v-icon>
                  </template>

                  <v-list-item-title class="wrap-list-item-title">
                    {{ field.flattenedDisplayName || field.displayName }}
                  </v-list-item-title>
                  <template v-slot:append>
                    <v-icon small @click.stop="toggleDescription(key)"
                      >mdi-information-outline</v-icon
                    >
                  </template>
                  <v-expand-transition>
                    <v-list-item-subtitle
                      v-if="expandedItems[key]"
                      class="wrap-list-item-subtitle"
                    >
                      {{ field.filterDescription }}
                    </v-list-item-subtitle>
                  </v-expand-transition>
                </v-list-item>
              </template>
            </v-list>
          </v-container>
        </v-row>
      </v-col>
      <v-btn
        elevation="14"
        :disabled="Object.keys(selectedFields).length < 1"
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
  </v-container>
</template>

<script>
import {
  simpleFilterFields,
  objectTypes,
  coupledFilterFields,
  preselectGroups
} from '@/libs/definitions'
import { useTheme } from 'vuetify'
import axios from '@/libs/axios'
import { attrsMandatoryForExport } from '@/libs/graphql-query'
export default {
  props: {
    selectedFieldsFromPreviousSearch: Object,
    addedFiltersFromPreviousSearch: Array
  },
  emits: ['render-table', 'close'],
  data: () => ({
    addingFilter: false,
    selectedField: '',
    expandedItems: {},
    newFilter: {
      key: '',
      djangoLookupFilter: '',
      group: '',
      include: '',
      djangoApp: '',
      djangoModel: '',
      coupledFilters: []
    },
    addedFilters: [],
    objectTypes: objectTypes,
    simpleFilterFields: simpleFilterFields,
    coupledFilterFields: coupledFilterFields,
    allFields: { ...simpleFilterFields, ...coupledFilterFields },
    fieldsSearch: '',
    selectedFields: {},
    preselectGroups: preselectGroups,
    coupledFiltersAvailable: {}
  }),
  methods: {
    handleClick(field, key) {
      if (key in this.preselectGroups) {
        for (let fieldToPreselect of this.preselectGroups[key]) {
          this.selectedFields[fieldToPreselect] = this.allFields[fieldToPreselect]
        }
      } else {
        this.selectedFields[key] = field
      }
    },
    toggleDescription(key) {
      this.expandedItems[key] = !this.expandedItems[key]
    },
    async getOptions(selectedField) {
      if (selectedField.apiEndpoint) {
        const url = `/api/v1/${selectedField.apiEndpoint}`
        const djangoApp = selectedField.djangoApp
        const djangoModel = selectedField.djangoModel
        const djangoField = selectedField.djangoField
        const djangoLimitchoicesApp = selectedField.djangoLimitchoicesApp
          ? selectedField.djangoLimitchoicesApp
          : null
        const djangoLimitchoicesModel = selectedField.djangoLimitchoicesModel
          ? selectedField.djangoLimitchoicesModel
          : null
        const djangoLimitchoicesField = selectedField.djangoLimitchoicesField
          ? selectedField.djangoLimitchoicesField
          : null
        try {
          const response = await axios.get(url, {
            params: {
              djangoApp,
              djangoModel,
              djangoField,
              djangoLimitchoicesApp,
              djangoLimitchoicesModel,
              djangoLimitchoicesField
            }
          })
          console.log(
            `options for ${djangoApp} - ${djangoModel}.${djangoField} are:`,
            response.data
          )
          return response.data.filter((option) => option)
        } catch (error) {
          console.error(`Error fetching options from ${url} endpoint`, error)
        }
      } else {
        return []
      }
    },
    getHeadersToHide() {
      // Hide the __typename and id fields by default, also hide the novelFoodId field if user didnt select it
      const fieldsToHide = ['__typename', 'id']
      fieldsToHide.push(...Object.values(attrsMandatoryForExport))

      const isNovelFoodIdSelected = 'novelFoodId' in this.selectedFields

      if (!isNovelFoodIdSelected) {
        fieldsToHide.push('novelFoodId')
      }
      return fieldsToHide
    },
    addFilter() {
      if (this.allFiltersValid) {
        this.addedFilters.unshift(this.newFilter)
        this.addingFilter = false
        this.newFilter = {
          djangoLookupFilter: '',
          key: '',
          group: '',
          include: '',
          djangoApp: '',
          djangoModel: '',
          coupledFilters: []
        }
        this.coupledFiltersAvailable = {}
      }
    },
    addCoupledFilter() {
      this.newFilter.coupledFilters.push({
        key: '',
        qualifier: '',
        value: '',
        options: []
      })
    },

    async updateFilterKey() {
      if (Object.keys(this.simpleFilterFields).includes(this.newFilter.key)) {
        this.coupledFiltersAvailable = {}
        const selectedField = this.simpleFilterFields[this.newFilter.key]
        this.newFilter.group = selectedField.displayGroupName
        this.newFilter.coupledFilters = [
          {
            key: this.newFilter.key,
            qualifier: '',
            value: '',
            options: await this.getOptions(selectedField)
          }
        ]
        this.newFilter.djangoApp = ''
        this.newFilter.djangoModel = ''
        this.newFilter.djangoLookupFilter = ''
      } else if (Object.keys(this.objectTypes).includes(this.newFilter.key)) {
        const selectedField = this.objectTypes[this.newFilter.key]
        this.newFilter.djangoApp = selectedField.djangoApp
        this.newFilter.djangoModel = selectedField.djangoModel
        this.newFilter.djangoLookupFilter = selectedField.djangoLookupFilter
        this.newFilter.group = selectedField.displayGroupName
        this.newFilter.coupledFilters = [
          {
            key: '',
            qualifier: '',
            value: '',
            options: []
          }
        ]
        this.coupledFiltersAvailable = Object.fromEntries(
          Object.entries(this.coupledFilterFields).filter(([key, value]) =>
            key.startsWith(this.newFilter.key)
          )
        )
      }
    },
    async updateCoupledFilterKey(i) {
      let selectedCoupledField = this.coupledFilterFields[this.newFilter.coupledFilters[i].key]
      this.newFilter.coupledFilters[i].qualifier = ''
      this.newFilter.coupledFilters[i].value = ''
      this.newFilter.coupledFilters[i].options = await this.getOptions(selectedCoupledField)
    },
    cancelNewFilter() {
      this.addingFilter = false
      this.newFilter = {
        djangoLookupFilter: '',
        key: '',
        group: '',
        include: '',
        djangoApp: '',
        djangoModel: '',
        coupledFilters: []
      }
      this.coupledFiltersAvailable = {}
    },
    editFilter(i) {
      this.addingFilter = true
      this.newFilter = this.addedFilters[i]
      this.coupledFiltersAvailable = Object.fromEntries(
        Object.entries(this.coupledFilterFields).filter(([key, value]) =>
          key.startsWith(this.newFilter.key)
        )
      )
      this.removeFilter(i)
    },
    removeFilter(i) {
      this.addedFilters.splice(i, 1)
    },
    renderTable() {
      console.log('new this.addedFilters', this.addedFilters)
      this.$emit('render-table', this.addedFilters, this.selectedFields, this.getHeadersToHide())
      this.$emit('close')
    }
  },
  computed: {
    alertText() {
      if (Object.keys(this.selectedFields).length < 1) {
        return 'Select data you would like to see'
      } else if (Object.keys(this.selectedFields).length > 10) {
        return 'Selecting too many fields will result in a long time to fetch the data'
      } else {
        return false
      }
    },
    filtersItems() {
      return Object.entries({ ...this.simpleFilterFields, ...this.objectTypes })
        .filter(([key, field]) => field.showInFilters)
        .map(([key, field]) => ({
          key: key,
          displayName: field.flattenedDisplayName || field.displayName
        }))
    },
    coupledFiltersItems() {
      return Object.entries({ ...this.coupledFiltersAvailable })
        .filter(([key, field]) => field.showInFilters)
        .map(([key, field]) => ({
          key: key,
          displayName: field.flattenedDisplayName || field.displayName
        }))
    },
    allFieldsSelected() {
      return Object.keys(this.selectedFields).length === Object.keys(this.allFields).length
    },
    allFiltersValid() {
      return (
        this.newFilter.key &&
        this.newFilter.include &&
        this.newFilter.coupledFilters.every((filter) => {
          const hasBasicFields = filter.key && filter.qualifier
          const requiresValue = filter.qualifier !== 'is None'

          return requiresValue ? hasBasicFields && filter.value : hasBasicFields
        })
      )
    },
    fieldsSearched() {
      const fieldsSearch = this.fieldsSearch?.toLowerCase()

      if (!fieldsSearch) return this.allFields

      return Object.entries(this.allFields).reduce((acc, [key, field]) => {
        const nameUsed = field.flattenedDisplayName
          ? field.flattenedDisplayName.toLowerCase()
          : field.displayName.toLowerCase()

        if (nameUsed.indexOf(fieldsSearch) > -1) {
          acc[key] = field
        }

        return acc
      }, {})
    }
  },
  created() {
    this.theme = useTheme()
    // Properly initialize local copies from props when the component is created
    this.selectedFields = this.selectedFieldsFromPreviousSearch
      ? { ...this.selectedFieldsFromPreviousSearch }
      : {}
    this.addedFilters = this.addedFiltersFromPreviousSearch
      ? [...this.addedFiltersFromPreviousSearch]
      : []
  }
}
</script>
<style>
.wrap-list-item-title {
  white-space: normal;
  word-break: break-word;
  overflow-wrap: break-word;
}

.wrap-list-item-subtitle {
  display: block;
}

.wrap-text-in-chip {
  height: auto !important;
}

.wrap-text-in-chip .v-chip__content {
  line-height: 1.4;
  padding-top: 8px;
  padding-bottom: 8px;
  white-space: normal;
}
</style>
