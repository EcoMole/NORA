<template>
  <div>
    <h1>Database Search</h1>
  </div>

  <v-row v-if="showFilterInterface" class="mt-4">
    <v-col cols="7">
      <v-row class="d-flex justify-center">
        <h1 style="color: #a9a9a9">Novel Food Filters</h1>
      </v-row>

      <v-row class="mt-7">
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

      <v-row v-if="!addingFilter" class="d-flex justify-center">
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
          <v-card class="pa-2" rounded="xl" elevation="6" density="compact">
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
                      <span>which</span>
                      <v-autocomplete
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
                      ></v-text-field>
                    </v-row>
                  </v-col>

                  <v-col
                    v-if="availableFilters[newFilter.title]?.description"
                    cols="12"
                    class="text-center"
                  >
                    <p>
                      {{ availableFilters[newFilter.title]?.description }}
                    </p>
                  </v-col>
                </v-row>
              </v-container>
            </v-card-text>
            <v-card-actions class="mb-1 pt-0">
              <v-spacer></v-spacer>
              <v-btn color="tertiary" variant="tonal" @click="addingFilter = false">Cancel</v-btn>
              <v-btn
                color="secondary"
                :disabled="
                  !newFilter.include || !newFilter.title || !newFilter.qualifier || !newFilter.value
                "
                variant="elevated"
                class="mr-2 ml-5"
                @click="addFilter"
                >Save</v-btn
              >
            </v-card-actions>
          </v-card>
        </v-col>
      </v-row>
      <v-row v-for="(item, i) in addedFilters" :key="i" class="d-flex justify-end mb-0">
        <v-row class="d-flex justify-center mb-0" v-if="i != 0 || addingFilter == true">
          <span class="mt-0">and</span>
        </v-row>
        <v-col cols="12" class="mb-0 mr-1">
          <v-card
            border
            class="pa-2 mb-0"
            elevation="3"
            style="position: relative; overflow: visible"
            rounded="xl"
          >
            <v-btn
              :style="{ position: 'absolute', right: '+8px' }"
              fab
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
              {{ item.group }}
            </v-card-subtitle>
            <v-card-text class="pt-0 mt-0">
              Novel Foods <b>{{ item.include }}</b> {{ ' ' }}
              <v-chip rounded="pill" density="compact" class="pb-1" color="secondary">{{
                item.title
              }}</v-chip
              >{{ ' ' }}which <b>{{ item.qualifier }}</b
              >{{ ' ' }}
              <v-chip rounded="pill" density="compact" class="pb-1" color="secondary">{{
                item.value
              }}</v-chip>
            </v-card-text>
          </v-card>
        </v-col>
      </v-row>
    </v-col>
    <v-divider :thickness="2" vertical class="ml-0"></v-divider>
    <v-col cols="4">
      <v-row class="d-flex justify-center">
        <h1 style="color: #a9a9a9">Novel Food Data</h1>
      </v-row>
      <v-row>
        <v-container>
          <v-alert
            class="mb-3"
            v-if="selected.length < 1"
            icon="$warning"
            text="Select data you would like to see"
            type="secondary"
            density="“compact”"
            rounded="md"
          ></v-alert>
          <v-row v-if="selected.length > 1 ? true : false" class="mb-2">
            <v-spacer></v-spacer>
            <v-btn
              @click="selected = []"
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
          <v-row align="center" justify="start">
            <v-col
              v-for="(selection, i) in selections"
              :key="selection.text"
              class="py-1 pe-0"
              cols="auto"
            >
              <v-chip
                :disabled="loading"
                size="large"
                closable
                elevation="3"
                @click:close="selected.splice(i, 1)"
                variant="elevated"
                :color="this.theme.global.current.value.dark ? 'black' : 'white'"
              >
                <v-icon :icon="selection.icon" start></v-icon>

                {{ selection.text }}
              </v-chip>
            </v-col>
          </v-row>
        </v-container>

        <v-container class="mt-4">
          <v-text-field
            v-if="!allSelected"
            ref="searchField"
            v-model="search"
            density="comfortable"
            placeholder="Search available data"
            prepend-inner-icon="mdi-magnify"
            style="max-width: 300px"
            variant="outlined"
            clearable
            hide-descriptions
          ></v-text-field>
          <v-list bg-color="rgba(0, 0, 0, 0)" density="compact">
            <template v-for="item in categories">
              <v-list-item
                v-if="!selected.includes(item)"
                :key="item.text"
                :disabled="loading"
                @click="selected.push(item)"
              >
                <template v-slot:prepend>
                  <v-icon :disabled="loading" :icon="item.icon"></v-icon>
                </template>

                <v-list-item-title v-text="item.text"></v-list-item-title>
              </v-list-item>
            </template>
          </v-list>
        </v-container>
      </v-row>
    </v-col>
    <v-btn
      elevation="14"
      :disabled="selected.length < 1"
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

  <div v-else>
    <v-row class="justify-end">
      <v-btn min-height="50px" color="primary">
        <v-icon left>mdi-download</v-icon>
        Export
      </v-btn>
    </v-row>
    <v-row class="d-flex justify-center">
      <v-sheet elevation="1" class="mt-2">
        <v-data-table :headers="headers" :items="opinions"></v-data-table>
      </v-sheet>
    </v-row>
    <v-hover v-slot="{ isHovering, props }">
      <v-btn
        v-bind="props"
        :elevation="isHovering ? 14 : 4"
        @click="showFilterInterface = true"
        size="large"
        min-height="50px"
        color="tertiary"
        position="fixed"
        location="bottom right"
        class="mb-8 mr-10"
        :ripple="false"
      >
        <v-icon left>mdi-replay</v-icon>
        new search
      </v-btn>
    </v-hover>
  </div>
</template>

<script>
import { useTheme } from 'vuetify'

// icon: 'mdi-rice'
// icon: 'mdi-alert-outline'
// icon: 'mdi-hazard-lights'
// icon: 'mdi-shield-alert'

export default {
  data: () => ({
    open: ['Users'],
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
    items: [
      {
        // administrative
        text: 'NF Code',
        icon: 'mdi-file-document-outline'
      },
      {
        text: 'Novel Food Title',
        icon: 'mdi-file-document-outline'
      },
      {
        text: 'Opinion URL',
        icon: 'mdi-file-document-outline'
      },
      {
        text: 'Opinion DOI',
        icon: 'mdi-file-document-outline'
      },
      {
        text: 'Publication Date',
        icon: 'mdi-file-document-outline'
      },

      {
        // nutrition
        text: 'Has Nutri Disadvantage',
        icon: 'mdi-nutrition'
      },
      {
        // allergenicity
        text: 'Allergenicity',
        icon: 'mdi-peanut-off'
      },
      {
        // ADME
        text: 'ADME studies',
        icon: 'mdi-pill'
      },
      {
        // toxicology
        text: 'Was Tox Study Required',
        icon: 'mdi-test-tube'
      },
      {
        text: 'Endpoint studies',
        icon: 'mdi-test-tube'
      },
      {
        text: 'Genotox studies',
        icon: 'mdi-test-tube'
      },
      {
        text: 'Final Outcome',
        icon: 'mdi-test-tube'
      },
      {
        text: 'Final Outcome Remarks',
        icon: 'mdi-test-tube'
      }
    ],
    showOptions: [
      'Allergenicity',
      'NF Code',
      'Novel Food Title',
      'Was Tox Study Required',
      'Has Nutri Disadvantage',
      'Opinion URL',
      'Opinion DOI',
      'Publication Date',
      'ADME studies',
      'Endpoint studies',
      'Genotox studies',
      'Final Outcome',
      'Final Outcome Remarks'
    ],
    loading: false,
    search: '',
    selected: [],
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

    showInColumns: [],
    showIndescriptions: [],
    addedFilters: [],
    opinions: [
      {
        allergenicity: 'Low',
        nfCode: 'NF001',
        novelFoodTitle: 'Cultured Meat',
        wasToxStudyRequired: true,
        hasNutriDisadvantage: false,
        opinionURL: 'http://example.com/nf001',
        opinionDOI: '10.1234/nf001',
        publicationDate: '2022-01-01',
        admeStudies: 'Study A1, Study A2',
        endpointStudies: 'Study B1, Study B2',
        genotoxStudies: 'Study C1',
        finalOutcomes: 'Approved',
        finalOutcomeRemarks: 'No significant issues'
      },
      {
        allergenicity: 'High',
        nfCode: 'NF002, NF302',
        novelFoodTitle: 'Engineered Probiotics, Yeast Cultures',
        wasToxStudyRequired: 'true, false',
        hasNutriDisadvantage: 'true, true',
        opinionURL: 'http://example.com/nf002',
        opinionDOI: '10.1234/nf002',
        publicationDate: '2023-02-15',
        admeStudies: 'Study A3',
        endpointStudies: 'Study B3, Study B4',
        genotoxStudies: 'Study C2, Study C3',
        finalOutcomes: 'Rejected',
        finalOutcomeRemarks: 'High allergenicity concerns'
      },
      {
        allergenicity: 'Moderate, Low',
        nfCode: 'NF003',
        novelFoodTitle: 'Algae-based Omega 3',
        wasToxStudyRequired: false,
        hasNutriDisadvantage: false,
        opinionURL: 'http://example.com/nf003',
        opinionDOI: '10.1234/nf003',
        publicationDate: '2021-11-20',
        admeStudies: 'Study A4',
        endpointStudies: 'Study B5',
        genotoxStudies: 'Study C4',
        finalOutcomes: 'Approved',
        finalOutcomeRemarks: 'Nutritional benefits noted'
      },
      {
        allergenicity: 'Unknown',
        nfCode: 'NF004, NF010, NF003',
        novelFoodTitle: 'Synthetic Vanillin, Artificial Sweeteners, Algae-based Omega 3',
        wasToxStudyRequired: 'true, true, false',
        hasNutriDisadvantage: 'true, false, false',
        opinionURL: 'http://example.com/nf004',
        opinionDOI: '10.1234/nf004',
        publicationDate: '2020-06-12',
        admeStudies: 'Study A5',
        endpointStudies: 'Study B6, Study B7',
        genotoxStudies: 'Study C5, Study C6',
        finalOutcomes: 'Approved',
        finalOutcomeRemarks: 'Requires labeling'
      },
      {
        allergenicity: 'Low, Moderate',
        nfCode: 'NF005',
        novelFoodTitle: 'Insect Protein',
        wasToxStudyRequired: true,
        hasNutriDisadvantage: false,
        opinionURL: 'http://example.com/nf005',
        opinionDOI: '10.1234/nf005',
        publicationDate: '2022-03-22',
        admeStudies: 'Study A6, Study A7',
        endpointStudies: 'Study B8',
        genotoxStudies: 'Study C7',
        finalOutcomes: 'Approved',
        finalOutcomeRemarks: 'Sustainable protein source'
      },
      {
        allergenicity: 'Moderate',
        nfCode: 'NF006',
        novelFoodTitle: 'Fermented Soy',
        wasToxStudyRequired: false,
        hasNutriDisadvantage: false,
        opinionURL: 'http://example.com/nf006',
        opinionDOI: '10.1234/nf006',
        publicationDate: '2021-05-11',
        admeStudies: 'Study A8',
        endpointStudies: 'Study B9, Study B10',
        genotoxStudies: 'Study C8',
        finalOutcomes: 'Approved',
        finalOutcomeRemarks: 'Rich in probiotics'
      },
      {
        allergenicity: 'High',
        nfCode: 'NF007',
        novelFoodTitle: 'Genetically Modified Corn',
        wasToxStudyRequired: true,
        hasNutriDisadvantage: true,
        opinionURL: 'http://example.com/nf007',
        opinionDOI: '10.1234/nf007',
        publicationDate: '2019-08-30',
        admeStudies: 'Study A9',
        endpointStudies: 'Study B11, Study B12',
        genotoxStudies: 'Study C9',
        finalOutcomes: 'Rejected',
        finalOutcomeRemarks: 'Potential health risks'
      },
      {
        allergenicity: 'Low',
        nfCode: 'NF008',
        novelFoodTitle: 'Microalgae Protein',
        wasToxStudyRequired: false,
        hasNutriDisadvantage: false,
        opinionURL: 'http://example.com/nf008',
        opinionDOI: '10.1234/nf008',
        publicationDate: '2020-10-05',
        admeStudies: 'Study A10, Study A11',
        endpointStudies: 'Study B13',
        genotoxStudies: 'Study C10',
        finalOutcomes: 'Approved',
        finalOutcomeRemarks: 'High protein content'
      },
      {
        allergenicity: 'Moderate',
        nfCode: 'NF009',
        novelFoodTitle: 'Lab-grown Fish',
        wasToxStudyRequired: true,
        hasNutriDisadvantage: false,
        opinionURL: 'http://example.com/nf009',
        opinionDOI: '10.1234/nf009',
        publicationDate: '2023-01-15',
        admeStudies: 'Study A12',
        endpointStudies: 'Study B14, Study B15',
        genotoxStudies: 'Study C11',
        finalOutcomes: 'Approved',
        finalOutcomeRemarks: 'Eco-friendly alternative'
      },
      {
        allergenicity: 'High',
        nfCode: 'NF010',
        novelFoodTitle: 'Genetically Modified Soy',
        wasToxStudyRequired: true,
        hasNutriDisadvantage: true,
        opinionURL: 'http://example.com/nf010',
        opinionDOI: '10.1234/nf010',
        publicationDate: '2022-12-01',
        admeStudies: 'Study A13, Study A14',
        endpointStudies: 'Study B16',
        genotoxStudies: 'Study C12',
        finalOutcomes: 'Rejected',
        finalOutcomeRemarks: 'Health and environmental concerns'
      },
      {
        allergenicity: 'Low',
        nfCode: 'NF011',
        novelFoodTitle: 'Edible Insects',
        wasToxStudyRequired: false,
        hasNutriDisadvantage: false,
        opinionURL: 'http://example.com/nf011',
        opinionDOI: '10.1234/nf011',
        publicationDate: '2021-07-17',
        admeStudies: 'Study A15',
        endpointStudies: 'Study B17',
        genotoxStudies: 'Study C13',
        finalOutcomes: 'Approved',
        finalOutcomeRemarks: 'High in protein'
      },
      {
        allergenicity: 'Moderate',
        nfCode: 'NF012',
        novelFoodTitle: 'Cell-cultured Dairy',
        wasToxStudyRequired: true,
        hasNutriDisadvantage: false,
        opinionURL: 'http://example.com/nf012',
        opinionDOI: '10.1234/nf012',
        publicationDate: '2020-04-21',
        admeStudies: 'Study A16',
        endpointStudies: 'Study B18',
        genotoxStudies: 'Study C14',
        finalOutcomes: 'Approved',
        finalOutcomeRemarks: 'Dairy alternative'
      },
      {
        allergenicity: 'Unknown',
        nfCode: 'NF013',
        novelFoodTitle: 'Synthetic Caffeine',
        wasToxStudyRequired: true,
        hasNutriDisadvantage: true,
        opinionURL: 'http://example.com/nf013',
        opinionDOI: '10.1234/nf013',
        publicationDate: '2019-11-05',
        admeStudies: 'Study A17',
        endpointStudies: 'Study B19',
        genotoxStudies: 'Study C15',
        finalOutcomes: 'Rejected',
        finalOutcomeRemarks: 'Safety concerns'
      },
      {
        allergenicity: 'Low',
        nfCode: 'NF014',
        novelFoodTitle: 'Plant-based Egg',
        wasToxStudyRequired: false,
        hasNutriDisadvantage: false,
        opinionURL: 'http://example.com/nf014',
        opinionDOI: '10.1234/nf014',
        publicationDate: '2021-09-14',
        admeStudies: 'Study A18',
        endpointStudies: 'Study B20',
        genotoxStudies: 'Study C16',
        finalOutcomes: 'Approved',
        finalOutcomeRemarks: 'Vegan-friendly'
      },
      {
        allergenicity: 'High',
        nfCode: 'NF015',
        novelFoodTitle: 'Genetically Modified Wheat',
        wasToxStudyRequired: true,
        hasNutriDisadvantage: true,
        opinionURL: 'http://example.com/nf015',
        opinionDOI: '10.1234/nf015',
        publicationDate: '2023-04-07',
        admeStudies: 'Study A19',
        endpointStudies: 'Study B21',
        genotoxStudies: 'Study C17',
        finalOutcomes: 'Rejected',
        finalOutcomeRemarks: 'Potential allergenicity issues'
      }
    ]
  }),
  methods: {
    next() {
      this.loading = true

      setTimeout(() => {
        this.search = ''
        this.selected = []
        this.loading = false
      }, 2000)
    },
    renderTable() {
      this.updateHeaders()
      this.showFilterInterface = false
    },
    updateSubtitle() {
      const selectedAttribute = this.availableFilters[this.newFilter.title]
      if (selectedAttribute) {
        this.newFilter.group = selectedAttribute.group
      }
    },
    addFilter() {
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
    },
    removeItem(index) {
      this.addedFilters.splice(index, 1)
    },
    updateHeaders() {
      const allHeaders = [
        { title: 'Allergenicity', key: 'allergenicity' },
        { title: 'NF Code', key: 'nfCode' },
        { title: 'Novel Food Title', key: 'novelFoodTitle' },
        { title: 'Was Tox Study Required', key: 'wasToxStudyRequired' },
        { title: 'Has Nutri Disadvantage', key: 'hasNutriDisadvantage' },
        { title: 'Opinion URL', key: 'opinionURL' },
        { title: 'Opinion DOI', key: 'opinionDOI' },
        { title: 'Publication Date', key: 'publicationDate' },
        { title: 'ADME studies', key: 'admeStudies' },
        { title: 'Endpoint studies', key: 'endpointStudies' },
        { title: 'Genotox studies', key: 'genotoxStudies' },
        { title: 'Final Outcome', key: 'finalOutcomes' },
        { title: 'Final Outcome Remarks', key: 'finalOutcomeRemarks' }
      ]
      this.headers = allHeaders.filter((header) => this.showInColumns.includes(header.title))
    }
  },
  mounted() {
    this.updateHeaders()
  },
  computed: {
    allSelected() {
      return this.selected.length === this.items.length
    },
    categories() {
      const search = this.search.toLowerCase()

      if (!search) return this.items

      return this.items.filter((item) => {
        const text = item.text.toLowerCase()

        return text.indexOf(search) > -1
      })
    },
    selections() {
      const selections = []

      for (const selection of this.selected) {
        selections.push(selection)
      }

      return selections
    }
  },

  watch: {
    selected() {
      this.search = ''
    }
  },
  created() {
    this.theme = useTheme()
  }
}
</script>
