<template>
  <div>
    <h1>Opinions</h1>
  </div>
  <div v-if="showFilterInterface">
    <v-div>
      <v-container>
        <v-row class="mt-5">
          <v-col cols="9">
            <v-row>
              <v-combobox
                clearable
                chips
                multiple
                label="Display in columns"
                v-model="showInColumns"
                :items="showOptions"
              ></v-combobox>
            </v-row>
            <v-row>
              <v-combobox
                clearable
                chips
                multiple
                v-model="showInDetails"
                label="Display in details"
                :items="showOptions"
              ></v-combobox>
            </v-row>
          </v-col>
          <v-col cols="3">

            <v-row class="mt-8 justify-center">
              <v-btn @click="renderTable" style="min-height: 50px" color="secondary">
                <v-icon left>mdi-magnify</v-icon>
                Perform Search
              </v-btn>
            </v-row>
          </v-col>
        </v-row>
      </v-container>
    </v-div>

    <div class="mt-8">
      <v-data-iterator
        item-value="id"
        :items="createdFilters"
        :items-per-page="8"
        :search="searchFilter"
      >
        <template v-slot:header>
          <v-toolbar class="px-2" style="background-color: transparent">
            <v-text-field
              v-model="searchFilter"
              density="comfortable"
              placeholder="Search created filters"
              prepend-inner-icon="mdi-magnify"
              style="max-width: 300px"
              variant="solo"
              clearable
              hide-details
            ></v-text-field>
            <v-spacer></v-spacer>
            <v-btn color="primary" variant="outlined" @click="dialog = true">
              <v-icon left>mdi-plus</v-icon>
              Add Filter
            </v-btn>
          </v-toolbar>
        </template>
        <template v-slot:default="{ items }">
          <v-row>
            <v-col v-for="(item, i) in items" :key="i" cols="12" md="6">
              <v-card border>
                <v-card-title>
                  <h3>{{ item.raw.title }}</h3>
                </v-card-title>

                <v-card-text>
                  {{ item.raw.subtitle }}
                </v-card-text>

                <v-table density="compact" class="text-caption">
                  <thead>
                    <tr>
                      <th class="text-left">Include / Exclude</th>
                      <th class="text-left">Filter</th>
                      <th class="text-left">Qualifier</th>
                      <th class="text-left">Value</th>
                    </tr>
                  </thead>
                  <tbody>
                    <tr>
                      <td>
                        <b>{{ item.raw.include ? 'include' : 'exclude' }}</b>
                      </td>
                      <td>
                        <b>{{ item.raw.title }}</b>
                      </td>
                      <td>
                        <b>{{ item.raw.qualifier }}</b>
                      </td>
                      <td>
                        <b>{{ item.raw.value }}</b>
                      </td>
                    </tr>
                  </tbody>
                </v-table>

                <v-card-actions>
                  <v-spacer></v-spacer>
                  <v-btn color="tertiary" text @click="removeItem(i)">Remove</v-btn>
                </v-card-actions>
              </v-card>
            </v-col>
          </v-row>
        </template>

        <template v-slot:footer="{ page, pageCount, prevPage, nextPage }">
          <div class="d-flex align-center justify-center pa-4">
            <v-btn
              :disabled="page === 1"
              icon="mdi-arrow-left"
              density="comfortable"
              variant="tonal"
              rounded
              @click="prevPage"
            ></v-btn>

            <div class="mx-2 text-caption">Page {{ page }} of {{ pageCount }}</div>

            <v-btn
              :disabled="page >= pageCount"
              icon="mdi-arrow-right"
              density="comfortable"
              variant="tonal"
              rounded
              @click="nextPage"
            ></v-btn>
          </div>
        </template>
      </v-data-iterator>
    </div>

    <!-- Add Filter Dialog -->
    <v-dialog v-model="dialog" max-width="500px">
      <v-card>
        <v-card-title>
          <span class="headline"> {{ this.dataEntities[newFilter.title]?.subtitle || '' }}</span>
        </v-card-title>
        <v-card-text>
          <v-container>
            <v-row>
              <v-col cols="12">
                <v-select
                  v-model="newFilter.include"
                  :items="['include', 'exclude']"
                  label="Include / Exclude"
                ></v-select>
              </v-col>
              <v-col cols="12">
                <v-autocomplete
                  v-model="newFilter.title"
                  :items="Object.keys(dataEntities)"
                  label="Title"
                  @change="updateSubtitle"
                ></v-autocomplete>
              </v-col>

              <v-col cols="12">
                <v-autocomplete
                  v-model="newFilter.qualifier"
                  :items="dataEntities[newFilter.title]?.qualifiers || []"
                  label="Qualifier"
                ></v-autocomplete>
              </v-col>
              <v-col cols="12">
                <v-text-field v-model="newFilter.value" label="Value"></v-text-field>
              </v-col>
              <v-col cols="12">
                <p>
                  {{ this.dataEntities[newFilter.title]?.detail || '' }}
                </p>
              </v-col>
            </v-row>
          </v-container>
        </v-card-text>
        <v-card-actions>
          <v-spacer></v-spacer>
          <v-btn color="secondary" text @click="dialog = false">Close</v-btn>
          <v-btn color="primary" text @click="addFilter">Save</v-btn>
        </v-card-actions>
      </v-card>
    </v-dialog>
  </div>
  <div v-if="!showFilterInterface">
    <v-row class="mb-8">
      <v-col cols="4"> </v-col>
      <v-col cols="4">
        <v-row class="justify-center">
          <v-btn @click="showFilterInterface = true" style="min-height: 50px" color="secondary">
            <v-icon left>mdi-replay</v-icon>
            new search
          </v-btn>
        </v-row>
      </v-col>
      <v-col cols="4">
        <v-row class="justify-center">
          <v-btn style="min-height: 50px" color="primary">
            <v-icon left>mdi-export</v-icon>
            Export
          </v-btn>
        </v-row>
      </v-col>

    </v-row>

    <v-row class="d-flex justify-center">
      <v-sheet elevation="1" class="mt-2">
        <v-data-table v-model:sort-by="sortBy" :headers="headers" :items="opinions"></v-data-table>
      </v-sheet>
    </v-row>
  </div>
</template>

<script>
export default {
  data: () => ({
    showFilterInterface: true,
    searchFilter: '',
    dialog: false,
    headers: [],
    newFilter: {
      include: "",
      title: '',
      subtitle: '',
      qualifier: '',
      value: ''
    },
    dataEntities: {
      'production process': {
        subtitle: 'production process',
        qualifiers: ['contains', 'is'],
        detail:
          'this is more information and explanation about the filter user has just selected. It explains the attribute which will be queried, what values it can hold, etc.'
      },
      'opinion regulation': {
        subtitle: 'administrative',
        qualifiers: ['contains', 'is'],
        detail:
          'this is more information and explanation about the filter user has just selected. It explains the attribute which will be queried, what values it can hold, etc.'
      },
      'date of publication': {
        subtitle: 'administrative',
        qualifiers: ['is', 'greater than', 'less than'],
        detail:
          'this is more information and explanation about the filter user has just selected. It explains the attribute which will be queried, what values it can hold, etc.'
      },
      'type mandate': {
        subtitle: 'administrative',
        qualifiers: ['contains', 'is'],
        detail:
          'this is more information and explanation about the filter user has just selected. It explains the attribute which will be queried, what values it can hold, etc.'
      }
    },
    expandedItems: {},
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
    showInColumns: [],
    showInDetails: [],
    createdFilters: [
      {
        id: 1,
        include: true,
        title: 'production process',
        subtitle: 'production process',
        qualifier: 'contains',
        value: 'solvent steps'
      },
      {
        id: 2,
        include: false,
        title: 'production process',
        subtitle: 'production process',
        qualifier: 'contains',
        value: 'enzymes'
      },
      {
        id: 3,
        include: true,
        title: 'date of publication',
        subtitle: 'administrative',
        qualifier: 'greater than',
        value: '01.07.2018'
      },
      {
        id: 4,
        include: false,
        title: 'type mandate',
        subtitle: 'administrative',
        qualifier: 'is',
        value: 'extension of use'
      },
      {
        id: 6,
        include: true,
        title: 'opinion regulation',
        subtitle: 'administrative',
        qualifier: 'is',
        value: 'Regulation (EC) No 2015/2283 Article 10'
      },
    ],
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
        wasToxStudyRequired: "true, false",
        hasNutriDisadvantage: "true, true",
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
        wasToxStudyRequired: "true, true, false",
        hasNutriDisadvantage: "true, false, false",
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
    renderTable() {
      this.updateHeaders()
      this.showFilterInterface = false
    },
    updateSubtitle() {
      const selectedEntity = this.dataEntities[this.newFilter.title]
      if (selectedEntity) {
        this.newFilter.subtitle = selectedEntity.subtitle
      }
    },
    addFilter() {
      this.createdFilters.push({
        id: this.createdFilters.length + 1,
        include: this.newFilter.include,
        title: this.newFilter.title,
        subtitle: this.newFilter.subtitle,
        qualifier: this.newFilter.qualifier,
        value: this.newFilter.value
      })
      this.dialog = false
      this.newFilter = {
        include: true,
        title: '',
        subtitle: '',
        qualifier: '',
        value: ''
      }
    },
    removeItem(index) {
      this.createdFilters.splice(index, 1)
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
  }
}
</script>
