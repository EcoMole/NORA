<template>
  <v-container>
    <v-row class="mt-4">
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
                          @update:modelValue="updateFilter"
                        ></v-autocomplete>
                      </v-row>
                    </v-col>
                    <v-col cols="12">
                      <v-row class="d-flex align-center">
                        <span v-if="newFilter.key">which</span>
                        <v-autocomplete
                          :disabled="!newFilter.key"
                          v-model="newFilter.qualifier"
                          :items="fields[newFilter.key]?.qualifiers || []"
                          max-width="180px"
                          variant="underlined"
                          class="ml-6"
                        ></v-autocomplete>
                        <v-autocomplete
                          v-if="showOptionsListField"
                          v-model="newFilter.value"
                          :items="newFilter.options"
                          max-width="180px"
                          variant="underlined"
                          class="ml-6"
                        ></v-autocomplete>
                        <v-text-field
                          v-if="showValueField"
                          variant="underlined"
                          v-model="newFilter.value"
                          :type="fields[newFilter.key]?.type"
                          class="ml-6"
                          :disabled="!newFilter.key"
                        ></v-text-field>
                      </v-row>
                    </v-col>

                    <v-col v-if="fields[newFilter.key]?.filterDescription" cols="12">
                      <p>
                        {{ fields[newFilter.key].filterDescription }}
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
                  filter.title
                }}</v-chip
                >{{ ' ' }}which <b>{{ filter.qualifier }}</b
                >{{ ' ' }}
                <v-chip
                  v-if="filter.value"
                  rounded="pill"
                  density="compact"
                  class="pb-1"
                  color="secondary"
                  >{{ filter.value }}</v-chip
                >
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
              v-if="Object.keys(selectedFields).length < 1"
              icon="$warning"
              text="Select data you would like to see"
              color="secondary"
              rounded="md"
            ></v-alert>
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
                <v-tooltip :text="field.tooltipDescription" location="left">
                  <template v-slot:activator="{ props }">
                    <v-col class="py-1 pe-0" cols="auto">
                      <v-chip
                        v-bind="props"
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
                </v-tooltip>
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
              <v-tooltip
                text="Selecting all filelds will result in long time to fetch the data"
                location="top"
              >
                <template v-slot:activator="{ props }">
                  <v-btn
                    v-bind="props"
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
                </template>
              </v-tooltip>
            </v-row>
            <v-list bg-color="rgba(0, 0, 0, 0)" density="compact">
              <template v-for="(field, key) in fieldsSearched" :key="key">
                <v-tooltip
                  :text="field.tooltipDescription"
                  v-model="tooltipVisibility[key]"
                  location="left"
                >
                  <template v-slot:activator="{ props }">
                    <v-list-item
                      v-bind="props"
                      v-show="!(key in selectedFields)"
                      :key="key"
                      @click="handleClick(field, key)"
                    >
                      <template v-slot:prepend>
                        <v-icon :icon="field.icon"></v-icon>
                      </template>

                      <v-list-item-title>{{
                        field.flattenedDisplayName ? field.flattenedDisplayName : field.displayName
                      }}</v-list-item-title>
                    </v-list-item>
                  </template>
                </v-tooltip>
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
import { fields } from '@/libs/definitions'
import { useTheme } from 'vuetify'
import axios from '@/libs/axios'
export default {
  props: {
    selectedFieldsFromPreviousSearch: Object,
    addedFiltersFromPreviousSearch: Array
  },
  emits: ['render-table', 'close'],
  data: () => ({
    addingFilter: false,
    selectedField: '',
    filter: '',
    newFilter: {
      key: '',
      include: '',
      title: '',
      group: '',
      qualifier: '',
      value: '',
      options: []
    },
    addedFilters: [],
    fields: fields,
    fieldsSearch: '',
    selectedFields: {},
    tooltipVisibility: {}
  }),
  methods: {
    handleClick(field, key) {
      this.tooltipVisibility[key] = false
      this.selectedFields[key] = field
    },
    async getOptions(
      apiEndpoint,
      djangoApp,
      djangoModel,
      djangoField,
      djangoLimitchoicesApp,
      djangoLimitchoicesModel,
      djangoLimitchoicesField
    ) {
      const url = `/api/v1/${apiEndpoint}`
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
        console.log(`options for ${djangoApp} - ${djangoModel}.${djangoField} are:`, response.data)
        return response.data.filter((option) => option)
      } catch (error) {
        console.error(`Error fetching options from ${apiEndpoint} endpoint`, error)
      }
    },
    getHeadersToHide() {
      // Hide the __typename and id fields by default, also hide the novelFoodId field if user didnt select it
      const fieldsToHide = ['__typename', 'id']

      const isNovelFoodIdSelected = 'novelFoodId' in this.selectedFields

      if (!isNovelFoodIdSelected) {
        fieldsToHide.push('novelFoodId')
      }
      return fieldsToHide
    },
    addFilter() {
      if (this.addFilterValid) {
        this.addedFilters.unshift({
          id: this.addedFilters.length + 1,
          key: this.newFilter.key,
          include: this.newFilter.include,
          title: this.newFilter.title,
          group: this.newFilter.group,
          qualifier: this.newFilter.qualifier,
          value: this.newFilter.qualifier === 'is None' ? '' : this.newFilter.value
        })
        this.addingFilter = false
        this.newFilter = {
          key: '',
          include: '',
          title: '',
          group: '',
          qualifier: '',
          value: '',
          options: []
        }
      }
    },
    async updateFilter() {
      const selectedField = this.fields[this.newFilter.key]

      if (selectedField) {
        this.newFilter.title = selectedField.flattenedDisplayName || selectedField.displayName
        this.newFilter.qualifier =
          selectedField.qualifiers.length === 1 ? selectedField.qualifiers[0] : ''
        this.newFilter.group = selectedField.displayGroupName
        this.newFilter.value = ''
        if (selectedField.apiEndpoint) {
          const djangoLimitchoicesApp = selectedField.djangoLimitchoicesApp
            ? selectedField.djangoLimitchoicesApp
            : null
          const djangoLimitchoicesModel = selectedField.djangoLimitchoicesModel
            ? selectedField.djangoLimitchoicesModel
            : null
          const djangoLimitchoicesField = selectedField.djangoLimitchoicesField
            ? selectedField.djangoLimitchoicesField
            : null
          this.newFilter.options = await this.getOptions(
            selectedField.apiEndpoint,
            selectedField.djangoApp,
            selectedField.djangoModel,
            selectedField.djangoField,
            djangoLimitchoicesApp,
            djangoLimitchoicesModel,
            djangoLimitchoicesField
          )
        }
      }
    },
    cancelNewFilter() {
      this.addingFilter = false
      this.newFilter = {
        include: '',
        key: '',
        title: '',
        group: '',
        qualifier: '',
        value: '',
        options: []
      }
    },
    editFilter(index) {
      this.addingFilter = true
      this.newFilter = {
        include: this.addedFilters[index].include,
        key: this.addedFilters[index].key,
        title: this.addedFilters[index].title,
        group: this.addedFilters[index].group,
        qualifier: this.addedFilters[index].qualifier,
        value: this.addedFilters[index].value,
        options: this.addedFilters[index].options ? this.addedFilters[index].options : []
      }
      this.removeFilter(index)
    },
    removeFilter(index) {
      this.addedFilters.splice(index, 1)
    },
    renderTable() {
      this.$emit('render-table', this.addedFilters, this.selectedFields, this.getHeadersToHide())
      this.$emit('close')
    }
  },
  computed: {
    showOptionsListField() {
      return this.newFilter.options.length > 0 && this.newFilter.qualifier !== 'is None'
    },
    showValueField() {
      return this.newFilter.options.length < 1 && this.newFilter.qualifier !== 'is None'
    },
    filtersItems() {
      return (
        Object.entries(this.fields)
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
        this.newFilter.include && this.newFilter.title && this.newFilter.qualifier
      const hasValue = this.newFilter.value
      if (this.newFilter.qualifier != 'is None') {
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
    for (const key in this.fields) {
      this.tooltipVisibility[key] = false
    }
  }
}
</script>
