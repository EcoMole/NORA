<template>
  <v-container>
    <v-btn @click="print">print</v-btn>
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
                {{ this.newFilter.coupledFilters[0].group }}
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
                          v-model="newFilter.coupledFilters[0].key"
                          :items="filtersItems"
                          item-title="displayName"
                          item-value="key"
                          class="ml-6"
                          variant="underlined"
                          @update:modelValue="updateFilterKey"
                          ><template v-slot:append>
                            <v-icon small>mdi-information-outline</v-icon>
                          </template></v-autocomplete
                        >
                      </v-row>
                    </v-col>
                    <!-- <v-col cols="12">
                      <v-row class="d-flex align-center">
                        <span>with</span>
                        <v-autocomplete
                          v-model="newFilter.coupledFilters[0].key"
                          :items="filtersItems"
                          item-title="displayName"
                          item-value="key"
                          class="ml-6"
                          variant="underlined"
                          @update:modelValue="updateFilterKey"
                          ><template v-slot:append>
                            <v-icon small>mdi-information-outline</v-icon>
                          </template></v-autocomplete
                        >
                      </v-row>
                    </v-col> -->
                    <v-col cols="12">
                      <v-row class="d-flex align-center">
                        <span v-if="newFilter.coupledFilters[0].key">which</span>
                        <v-autocomplete
                          :disabled="!newFilter.coupledFilters[0].key"
                          v-model="newFilter.coupledFilters[0].qualifier"
                          :items="fields[newFilter.coupledFilters[0].key]?.qualifiers || []"
                          max-width="150px"
                          variant="underlined"
                          class="ml-6"
                          @update:modelValue="updateFilterQualifier"
                        ></v-autocomplete>
                        <v-autocomplete
                          v-if="showOptionsListField"
                          v-model="newFilter.coupledFilters[0].value"
                          :items="newFilter.coupledFilters[0].options"
                          variant="underlined"
                          class="ml-6"
                        ></v-autocomplete>
                        <v-text-field
                          v-if="showValueField"
                          variant="underlined"
                          v-model="newFilter.coupledFilters[0].value"
                          :type="fields[newFilter.coupledFilters[0].key]?.type"
                          class="ml-6"
                          :disabled="!newFilter.coupledFilters[0].key"
                        ></v-text-field>
                      </v-row>
                    </v-col>

                    <v-col
                      v-if="fields[newFilter.coupledFilters[0].key]?.filterDescription"
                      cols="12"
                    >
                      <p>
                        {{ fields[newFilter.coupledFilters[0].key].filterDescription }}
                      </p>
                    </v-col>
                  </v-row>
                  <!-- <v-row class="d-flex justify-center mt-5">
                    <v-btn color="secondary" variant="tonal" @click="addingFilter = true">
                      and with..
                    </v-btn>
                  </v-row>
                  <v-row class="d-flex justify-center mb-0" v-if="true">
                    <span class="mt-0">and</span>
                  </v-row> -->
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
                @click="removeFilter(i)"
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
                @click="editFilter(i)"
                variant="tonal"
                style="z-index: 2"
              >
                edit
              </v-btn>
              <v-card-subtitle class="text-h6 pt-3 pb-2 mb-0">
                {{ filter.group }}
              </v-card-subtitle>
              <v-card-text class="pt-0">
                Novel Foods <b>{{ filter.include }}</b> {{ ' ' }}
                <v-chip rounded="pill" density="compact" class="pb-1" color="secondary">{{
                  filter.coupledFilters[0].title
                }}</v-chip
                >{{ ' ' }}which <b>{{ filter.coupledFilters[0].qualifier }}</b
                >{{ ' ' }}
                <v-chip
                  v-if="filter.coupledFilters[0].value"
                  rounded="pill"
                  density="compact"
                  class="pb-1"
                  color="secondary"
                  >{{ filter.coupledFilters[0].value }}</v-chip
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
                @click="selectedFields = fields"
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

                  <v-list-item-title class="wrap-text">
                    {{ field.flattenedDisplayName || field.displayName }}
                  </v-list-item-title>
                  <template v-slot:append>
                    <v-icon small @click.stop="toggleDescription(key)"
                      >mdi-information-outline</v-icon
                    >
                  </template>
                  <v-expand-transition>
                    <v-list-item-subtitle v-if="expandedItems[key]" class="wrap-text">
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
import { novelFoodAndOpinionFields, objectTypes, fields, preselectGroups } from '@/libs/definitions'
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
    filter: '',
    // newFilter: {
    //   key: '',
    //   include: '',
    //   title: '',
    //   group: '',
    //   qualifier: '',
    //   value: '',
    //   options: []
    // },
    newFilter: {
      djangoLookupFilter: '',
      include: '',
      djangoApp: '',
      djangoModel: '',
      coupledFilters: [
        {
          key: '',
          title: '',
          group: '',
          qualifier: '',
          value: '',
          options: []
        }
      ]
    },
    addedFilters: [],
    novelFoodAndOpinionFields: novelFoodAndOpinionFields,
    // objectTypes: objectTypes,
    fields: { ...novelFoodAndOpinionFields, ...fields },
    fieldsSearch: '',
    selectedFields: {},
    preselectGroups: preselectGroups
  }),
  methods: {
    print() {
      console.log('addedFilters', this.addedFilters)
    },
    handleClick(field, key) {
      if (key in this.preselectGroups) {
        for (let fieldToPreselect of this.preselectGroups[key]) {
          this.selectedFields[fieldToPreselect] = this.fields[fieldToPreselect]
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
          this.newFilter.coupledFilters[0].options = response.data.filter((option) => option)
        } catch (error) {
          console.error(`Error fetching options from ${url} endpoint`, error)
        }
      } else {
        this.newFilter.coupledFilters[0].options = []
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
      if (this.addFilterValid) {
        // this.addedFilters.unshift({
        //   id: this.addedFilters.length + 1,
        //   key: this.newFilter.key,
        //   include: this.newFilter.include,
        //   title: this.newFilter.title,
        //   group: this.newFilter.group,
        //   qualifier: this.newFilter.qualifier,
        //   value: this.newFilter.qualifier === 'is None' ? '' : this.newFilter.value
        // })
        this.addedFilters.unshift({
          id: this.addedFilters.length + 1,
          djangoLookupFilter: this.newFilter.djangoLookupFilter,
          include: this.newFilter.include,
          djangoApp: this.newFilter.djangoApp,
          djangoModel: this.newFilter.djangoModel,
          coupledFilters: this.newFilter.coupledFilters.map((filter) => ({
            key: filter.key,
            title: filter.title,
            group: filter.group,
            qualifier: filter.qualifier,
            value: filter.value
          }))
        })
        this.addingFilter = false
        this.newFilter = {
          djangoLookupFilter: '',
          include: '',
          djangoApp: '',
          djangoModel: '',
          coupledFilters: [
            {
              key: '',
              title: '',
              group: '',
              qualifier: '',
              value: '',
              options: []
            }
          ]
        }
      }
    },
    async updateFilterQualifier() {
      const selectedField = this.fields[this.newFilter.coupledFilters[0].key]

      if (selectedField) {
        await this.getOptions(selectedField)
      }
    },
    async updateFilterKey() {
      const selectedField = this.fields[this.newFilter.coupledFilters[0].key]

      if (selectedField) {
        this.newFilter.coupledFilters[0].title =
          selectedField.flattenedDisplayName || selectedField.displayName
        this.newFilter.coupledFilters[0].qualifier =
          selectedField.qualifiers.length === 1 ? selectedField.qualifiers[0] : ''
        this.newFilter.coupledFilters[0].group = selectedField.displayGroupName
        this.newFilter.coupledFilters[0].value = ''
        await this.getOptions(selectedField)
      }
    },
    cancelNewFilter() {
      this.addingFilter = false
      this.newFilter = {
        djangoLookupFilter: '',
        include: '',
        djangoApp: '',
        djangoModel: '',
        coupledFilters: [
          {
            key: '',
            title: '',
            group: '',
            qualifier: '',
            value: '',
            options: []
          }
        ]
      }
    },
    editFilter(index) {
      this.addingFilter = true
      this.newFilter = {
        djangoLookupFilter: this.addedFilters[index].djangoLookupFilter,
        coupledFilters: this.addedFilters[index].coupledFilters
      }
      const selectedField = this.fields[this.newFilter.coupledFilters[0].key]
      this.getOptions(selectedField)
      this.removeFilter(index)
    },
    removeFilter(index) {
      this.addedFilters.splice(index, 1)
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
    showOptionsListField() {
      return (
        this.newFilter.coupledFilters[0].options.length > 0 &&
        this.newFilter.coupledFilters[0].qualifier !== 'is None'
      )
    },
    showValueField() {
      return (
        this.newFilter.coupledFilters[0].options.length < 1 &&
        this.newFilter.coupledFilters[0].qualifier !== 'is None'
      )
    },
    filtersItems() {
      return (
        Object.entries({ ...this.novelFoodAndOpinionFields }) // ...this.objectTypes
          // filterout fields which are not showInFilters
          .filter((entry) => entry[1].showInFilters)
          .map(([key, field]) => ({
            key: key,
            displayName: field.flattenedDisplayName || field.displayName
          }))
      )
    },
    allFieldsSelected() {
      return Object.keys(this.selectedFields).length === Object.keys(this.fields).length
    },
    addFilterValid() {
      const hasNecessaryFields =
        this.newFilter.include &&
        this.newFilter.coupledFilters[0].title &&
        this.newFilter.coupledFilters[0].qualifier
      const hasValue = this.newFilter.coupledFilters[0].value
      if (this.newFilter.coupledFilters[0].qualifier != 'is None') {
        return hasNecessaryFields && hasValue
      } else {
        return hasNecessaryFields
      }
    },
    fieldsSearched() {
      const fieldsSearch = this.fieldsSearch?.toLowerCase()

      if (!fieldsSearch) return this.fields

      return Object.entries(this.fields).reduce((acc, [key, field]) => {
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
.wrap-text {
  white-space: normal;
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
