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
    <v-sheet elevation="2" class="mt-2 pa-4">
      <!-- v-slot is a directive in Vue.js that allows you to define a slot in a component. Slots are placeholders that you can fill with content when using the component. When using v-slot, you are essentially injecting custom content into a specific part of a child component. -->
      <!-- The { item } represents the entire object (row) for the current item in the table. -->
      <div>
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
              <template v-if="item[key] != null">
                <!-- table inside Opinion table -->
                <!-- documentType, title, doi, url, atd. -->
                <!-- key here is Opinion a item[key] is content of Opinion column -->
                <!-- content of opinion is allways object -->
                <v-data-table
                  :headers="createHeaders(item[key])"
                  :items="[item[key]]"
                  style="font-size: 10px"
                  density="compact"
                  hide-default-footer
                >
                  <!-- column creation documentType, doi, url -->
                  <template
                    v-for="(key, index) in Object.keys(item[key])"
                    v-slot:[`item.${key}`]="{ item }"
                    :key="`2-${index}`"
                  >
                    <div>
                      <template v-if="item[key] != null && typeof item[key] === 'object'">
                        <v-data-table
                          :headers="
                            createHeaders(Array.isArray(item[key]) ? item[key][0] : item[key])
                          "
                          :items="Array.isArray(item[key]) ? item[key] : [item[key]]"
                          style="font-size: 10px"
                          density="compact"
                          hide-default-footer
                        >
                        </v-data-table>
                      </template>
                      <template v-else>
                        {{ item[key] }}
                      </template>
                    </div>
                  </template>
                </v-data-table>
              </template>
              <template v-else>
                {{ item[key] }}
              </template>
            </div>
          </template>
        </v-data-table>
      </div>

      <!-- the old table variant -->
      <v-skeleton-loader
        v-if="!fetchedNovelFoods"
        class="mx-auto"
        type="table-thead, table-tbody, table-tbody, table-tbody"
        style="z-index: 0"
      ></v-skeleton-loader>
      <v-data-table
        v-if="fetchedNovelFoods && tableStyle != 'repeated'"
        :headers="firstLevelHeaders"
        :items="firstLevelData"
        style="font-size: 12px"
        density="compact"
      >
        <template v-slot:[`item.firstLevelColumn1Content`]="{ item }">
          <v-sheet>
            <v-data-table
              style="font-size: 12px"
              density="compact"
              hide-default-footer
              :headers="secondLevelHeaders1"
              :items="item.firstLevelColumn1Content"
            >
              <template v-slot:[`item.secondLevelColumn2Content`]="{ item }">
                <v-sheet>
                  <v-data-table
                    style="font-size: 12px"
                    density="compact"
                    hide-default-footer
                    :headers="thirdLevelHeaders1"
                    :items="item.secondLevelColumn2Content"
                  ></v-data-table>
                </v-sheet> </template
            ></v-data-table>
          </v-sheet>
        </template>
        <template v-slot:[`item.firstLevelColumn2Content`]="{ item }">
          <v-sheet>
            <v-data-table
              style="font-size: 12px"
              density="compact"
              hide-default-footer
              :headers="secondLevelHeaders2"
              :items="item.firstLevelColumn2Content"
            ></v-data-table>
          </v-sheet>
        </template>
        <template v-slot:[`item.firstLevelColumn3Content`]="{ item }">
          <v-sheet>
            <v-data-table
              style="font-size: 12px"
              density="compact"
              hide-default-footer
              :headers="secondLevelHeaders3"
              :items="item.firstLevelColumn3Content"
            ></v-data-table>
          </v-sheet>
        </template>
      </v-data-table>
    </v-sheet>

    <!-- DataTable tableStyle == repeated -->
    <v-row v-if="tableStyle == 'repeated'" class="d-flex justify-center">
      <v-sheet elevation="1" class="mt-2 pa-4">
        <v-data-table :headers="headers" :items="opinions"></v-data-table>
      </v-sheet>
    </v-row>

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
    firstLevelHeaders: [
      { title: 'NF code', value: 'nfCode', align: 'center' },
      { title: '', value: 'firstLevelColumn1Content', align: 'center' },
      { title: '', value: 'firstLevelColumn2Content', align: 'center' },
      { title: '', value: 'firstLevelColumn3Content', align: 'center' }
    ],
    secondLevelHeaders1: [
      { title: 'Question Number', value: 'secondLevelColumn1Content', align: 'center' },
      { title: '', value: 'secondLevelColumn2Content', align: 'center' }
    ],
    secondLevelHeaders2: [
      { title: 'ADME test material', value: 'secondLevelColumn1Content', align: 'center' },
      { title: 'ADME remarks', value: 'secondLevelColumn2Content', align: 'center' }
    ],
    secondLevelHeaders3: [
      {
        title: 'Final Outcome Uncertainity Factor',
        value: 'secondLevelColumn1Content',
        align: 'center'
      },
      { title: 'Final Outcome Remarks', value: 'secondLevelColumn2Content', align: 'center' }
    ],
    thirdLevelHeaders1: [
      { title: 'Applicant Name', value: 'thirdLevelColumn1Content', align: 'center' },
      { title: 'Applicant Surname', value: 'thirdLevelColumn2Content', align: 'center' }
    ],
    firstLevelData: [
      {
        nfCode: 'NF876897',
        firstLevelColumn1Content: [
          {
            secondLevelColumn1Content: 'Q 87687',
            secondLevelColumn2Content: [
              { thirdLevelColumn1Content: 'John', thirdLevelColumn2Content: 'Doe' },
              { thirdLevelColumn1Content: 'Bob', thirdLevelColumn2Content: 'Brown' }
            ]
          },
          {
            secondLevelColumn1Content: 'Q 867987',
            secondLevelColumn2Content: [
              { thirdLevelColumn1Content: 'John', thirdLevelColumn2Content: 'Doe' },
              { thirdLevelColumn1Content: 'Bob', thirdLevelColumn2Content: 'Brown' }
            ]
          }
        ],
        firstLevelColumn2Content: [
          { secondLevelColumn1Content: 'Value 1-5', secondLevelColumn2Content: 'Value 1-1' },
          { secondLevelColumn1Content: 'Value 1-3', secondLevelColumn2Content: 'Value 1-2' }
        ],
        firstLevelColumn3Content: [
          { secondLevelColumn1Content: 'Value 1-8', secondLevelColumn2Content: 'Value 1-1' },
          { secondLevelColumn1Content: 'Value 1-9', secondLevelColumn2Content: 'Value 1-2' }
        ]
      },
      {
        nfCode: 'NF768',
        firstLevelColumn1Content: [
          {
            secondLevelColumn1Content: 'Q 058967',
            secondLevelColumn2Content: [
              { thirdLevelColumn1Content: 'John', thirdLevelColumn2Content: 'Doe' },
              { thirdLevelColumn1Content: 'Bob', thirdLevelColumn2Content: 'Brown' }
            ]
          },
          {
            secondLevelColumn1Content: 'Q 97968',
            secondLevelColumn2Content: [
              { thirdLevelColumn1Content: 'John', thirdLevelColumn2Content: 'Doe' },
              { thirdLevelColumn1Content: 'Bob', thirdLevelColumn2Content: 'Brown' }
            ]
          }
        ],
        firstLevelColumn2Content: [
          { secondLevelColumn1Content: 'Sub-Item 2-1', secondLevelColumn2Content: 'Value 2-1' },
          { secondLevelColumn1Content: 'Sub-Item 2-2', secondLevelColumn2Content: 'Value 2-2' }
        ],
        firstLevelColumn3Content: [
          { secondLevelColumn1Content: 'Sub-Item 2-1', secondLevelColumn2Content: 'Value 2-1' },
          { secondLevelColumn1Content: 'Sub-Item 2-2', secondLevelColumn2Content: 'Value 2-2' }
        ]
      },
      {
        nfCode: 'NF987897',
        firstLevelColumn1Content: [
          {
            secondLevelColumn1Content: 'Q 876858',
            secondLevelColumn2Content: [
              { thirdLevelColumn1Content: 'John', thirdLevelColumn2Content: 'Doe' },
              { thirdLevelColumn1Content: 'Bob', thirdLevelColumn2Content: 'Brown' }
            ]
          },
          {
            secondLevelColumn1Content: 'Q 7658980',
            secondLevelColumn2Content: [
              { thirdLevelColumn1Content: 'John', thirdLevelColumn2Content: 'Doe' },
              { thirdLevelColumn1Content: 'Bob', thirdLevelColumn2Content: 'Brown' }
            ]
          }
        ],
        firstLevelColumn2Content: [
          { secondLevelColumn1Content: 'Sub-Item 2-1', secondLevelColumn2Content: 'Value 2-1' },
          { secondLevelColumn1Content: 'Sub-Item 2-2', secondLevelColumn2Content: 'Value 2-2' }
        ],
        firstLevelColumn3Content: [
          { secondLevelColumn1Content: 'Sub-Item 2-1', secondLevelColumn2Content: 'Value 2-1' },
          { secondLevelColumn1Content: 'Sub-Item 2-2', secondLevelColumn2Content: 'Value 2-2' }
        ]
      }
    ],
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
    availableAttrs: [
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
    ],
    fetchedNovelFoods: null
  }),
  methods: {
    createNestedTable(item) {
      return item !== null && typeof item === 'object' && !Array.isArray(item)
    },

    createHeaders(object) {
      if (!object) {
        return null
      } else {
        const headers = Object.keys(object)
          .filter((key) => key !== '__typename' && key !== 'id') // Exclude specific keys
          .map((key) => ({
            title: key,
            value: key,
            align: 'center'
          }))

        return headers
      }
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
      this.updateHeaders()
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
      this.headers = allHeaders.filter((header) =>
        this.selectedAttrs.map((attr) => attr.text).includes(header.title)
      )
    }
  },
  mounted() {
    this.updateHeaders()
  },
  computed: {
    allSelected() {
      return this.selectedAttrs.length === this.availableAttrs.length
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

      if (!availableAttrsSearch) return this.availableAttrs

      return this.availableAttrs.filter((attr) => {
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

<style scoped>
th {
  color: #557c55;
}
</style>
