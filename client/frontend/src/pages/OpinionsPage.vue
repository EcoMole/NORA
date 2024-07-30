<template>
  <div>
    <h1>Opinions</h1>
  </div>
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
              :items="[
                'Allergenicity',
                'NF Code',
                'Novel Food Title',
                'Was Tox Study Required',
                'Has Nutri Disadvantage',
                'Opinion URL',
                'Opinion doi',
                'Publication date'
              ]"
            ></v-combobox>
          </v-row>
          <v-row>
            <v-combobox
              clearable
              chips
              multiple
              v-model="showInDetails"
              label="Display in details"
              :items="[
                'ADME Studies',
                'Endpoint Studies',
                'Genotox Studies',
                'Final Outcomes',
                'Final Outcome Remarks'
              ]"
            ></v-combobox>
          </v-row>
        </v-col>
        <v-col cols="3">
          <v-row class="justify-center">
            <v-btn style="min-height: 50px" color="primary">
              <v-icon left>mdi-export</v-icon>
              Export
            </v-btn>
          </v-row>
          <v-row class="mt-8 justify-center">
            <v-btn style="min-height: 50px" color="secondary">
              <v-icon left>mdi-magnify</v-icon>
              Perform Search
            </v-btn>
          </v-row>
        </v-col>
      </v-row>
    </v-container>
  </v-div>

  <div class="mt-8">
    <v-data-iterator item-value="id" :items="novelFoods" :items-per-page="8" :search="searchFilter">
      <template v-slot:header>
        <v-toolbar class="px-2" style="background-color: transparent">
          <v-text-field
            v-model="searchFilter"
            density="comfortable"
            placeholder="Search chosen fileters"
            prepend-inner-icon="mdi-magnify"
            style="max-width: 300px"
            variant="solo"
            clearable
            hide-details
          ></v-text-field>
          <v-spacer></v-spacer>
          <v-btn color="primary" variant="outlined">
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
                <v-btn color="tertiary" text>Remove</v-btn>
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
</template>
<script>
export default {
  data: () => ({
    searchFilter: '',
    expandedItems: {},
    showInColumns: ['NF Code'],
    showInDetails: [],
    novelFoods: [
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
        title: 'opinion regulation',
        subtitle: 'administrative',
        qualifier: 'is',
        value: 'Regulation (EC) No 2015/2283 Article 10'
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
        id: 5,
        include: true,
        title: 'type mandate',
        subtitle: 'administrative',
        qualifier: 'is',
        value: 'nutrient source'
      },
      {
        id: 6,
        include: true,
        title: 'production process',
        subtitle: 'production process',
        qualifier: 'contains',
        value: 'microorganism'

      },
      {
        id: 7,
        include: false,
        title: 'production process',
        subtitle: 'production process',
        qualifier: 'contains',
        value: 'enzymes'
      }
    ]
  })
}
</script>
