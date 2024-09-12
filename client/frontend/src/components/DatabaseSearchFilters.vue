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
                @click="removeFilter(i)"
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
              v-if="Object.keys(selectedAttrs).length < 1"
              icon="$warning"
              text="Select data you would like to see"
              color="secondary"
              rounded="md"
            ></v-alert>
            <v-row v-if="Object.keys(selectedAttrs).length > 1" class="mb-2">
              <v-spacer></v-spacer>
              <v-btn
                @click="selectedAttrs = {}"
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
                v-for="(field, fieldPath) in selectedAttrs"
                :key="fieldPath"
                class="py-1 pe-0"
                cols="auto"
              >
                <v-chip
                  size="large"
                  closable
                  elevation="3"
                  @click:close="delete selectedAttrs[fieldPath]"
                  variant="elevated"
                  :color="this.theme.global.current.value.dark ? 'black' : 'white'"
                >
                  <v-icon :icon="field.icon" start></v-icon>

                  {{ field.displayName }}
                </v-chip>
              </v-col>
            </v-row>
          </v-container>

          <v-container class="mt-4">
            <v-text-field
              v-if="!allAttrsSelected"
              v-model="attrsSearch"
              density="comfortable"
              placeholder="Search available data"
              prepend-inner-icon="mdi-magnify"
              style="max-width: 300px"
              variant="outlined"
              clearable
              hide-details
            ></v-text-field>
            <v-list bg-color="rgba(0, 0, 0, 0)" density="compact">
              <template v-for="(field, fieldPath) in availableAttrsSearched">
                <v-list-item
                  v-if="!(fieldPath in selectedAttrs)"
                  :key="fieldPath"
                  @click="selectedAttrs[fieldPath] = field"
                >
                  <template v-slot:prepend>
                    <v-icon :icon="field.icon"></v-icon>
                  </template>

                  <v-list-item-title>{{ field.displayName }}</v-list-item-title>
                </v-list-item>
              </template>
            </v-list>
          </v-container>
        </v-row>
      </v-col>
      <v-btn
        elevation="14"
        :disabled="Object.keys(selectedAttrs).length < 1"
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
import { availableFilters } from '@/libs/available-filters'
import { newavailableAttrs } from '@/libs/available-attrs'
import { useTheme } from 'vuetify'
export default {
  props: {
    selectedAttrsFromPreviousSearch: Object,
    addedFiltersFromPreviousSearch: Array
  },
  data: () => ({
    availableFilters: availableFilters,
    addingFilter: false,
    newFilter: {
      include: '',
      title: '',
      group: '',
      qualifier: '',
      value: ''
    },
    addedFilters: [],
    newavailableAttrs: newavailableAttrs,
    attrsSearch: '',
    selectedAttrs: {},
    flattenedFields: {},
  }),
  methods: {
    addFilter() {
      if (this.addFilterValid) {
        this.addedFilters.unshift({
          id: this.addedFilters.length + 1,
          include: this.newFilter.include,
          title: this.newFilter.title,
          group: this.newFilter.group,
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
    updateSubtitle() {
      const selectedAttribute = this.availableFilters[this.newFilter.title]
      if (selectedAttribute) {
        this.newFilter.group = selectedAttribute.group
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
    removeFilter(index) {
      this.addedFilters.splice(index, 1)
    },
    renderTable() {
      this.$emit('render-table', this.addedFilters, this.selectedAttrs)
      this.$emit('close')
    },
    flattenFields(fields, parentPath = '') {
      let flatFields = {}
      for (let fieldName in fields) {
        let field = fields[fieldName]
        let currentPath = parentPath ? `${parentPath}.${fieldName}` : fieldName

        if (field.fields) {
          // Recursive call for nested fields
          flatFields = { ...flatFields, ...this.flattenFields(field.fields, currentPath) }
        } else {
          // Add field to flattened fields with its path
          flatFields[currentPath] = field
        }
      }
      return flatFields
    },
  },
  computed: {
    allAttrsSelected() {
      return Object.keys(this.selectedAttrs).length === Object.keys(this.flattenedFields).length
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
      const attrsSearch = this.attrsSearch?.toLowerCase()

      if (!attrsSearch) return this.flattenedFields

      return Object.entries(this.flattenedFields).reduce((acc, [fieldPath, field]) => {
        const displayName = field.displayName.toLowerCase()

        if (displayName.indexOf(attrsSearch) > -1) {
          acc[fieldPath] = field
        }

        return acc
      }, {})
    }
  },
  created() {
    this.theme = useTheme()
    // Properly initialize local copies from props when the component is created
    this.selectedAttrs = this.selectedAttrsFromPreviousSearch
      ? { ...this.selectedAttrsFromPreviousSearch }
      : {}
    this.addedFilters = this.addedFiltersFromPreviousSearch
      ? [...this.addedFiltersFromPreviousSearch]
      : []
    this.flattenedFields = this.flattenFields(this.newavailableAttrs.novelFoods.fields)
  }
}
</script>
