<template>
  <h1>Organism Identities</h1>
  <v-row class="mt-5">
    <v-col cols="8">
      <v-container>
        <v-row>
          <v-combobox
            clearable
            chips
            multiple
            label="Display in columns"
            v-model="showInColumns"
                      :items="['Genus', 'Family', 'Species', 'Is GMO']"
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
              'Remarks'
            ]"
          ></v-combobox>
        </v-row>
        <v-row>
          <v-sheet elevation="1" class="mt-2">
            <v-data-table
              v-model:sort-by="sortBy"
              :headers="headers"
              :items="organisms"
            ></v-data-table>
          </v-sheet>
        </v-row>
      </v-container>
    </v-col>
    <!-- <v-col cols="1"> </v-col> -->
    <SearchFilter @button-clicked="updateHeaders"></SearchFilter>
  </v-row>
</template>
<script>
import SearchFilter from '@/components/SearchFilter.vue'

export default {
  components: {
    SearchFilter
  },
  data() {
    return {
      showInColumns: ["Species"],
      showInDetails: [],
      headers: [],
      organisms: [
        {
          genus: 'Rosa',
          family: 'Rosaceae',
          species: 'R. rubiginosa',
          isGMO: false
        },
        {
          genus: 'Zea',
          family: 'Poaceae',
          species: 'Z. mays',
          isGMO: true
        },
        {
          genus: 'Triticum',
          family: 'Poaceae',
          species: 'T. aestivum',
          isGMO: false
        },
        {
          genus: 'Solanum',
          family: 'Solanaceae',
          species: 'S. tuberosum',
          isGMO: true
        },
        {
          genus: 'Oryza',
          family: 'Poaceae',
          species: 'O. sativa',
          isGMO: false
        }
      ]
    }
  },
  methods: {
    updateHeaders() {
      const allHeaders = [
        { title: 'Genus', key: 'genus' },
        { title: 'Family', key: 'family' },
        { title: 'Species', key: 'species' },
        { title: 'Is GMO', key: 'isGMO' }
      ];
      this.headers = allHeaders.filter(header => this.showInColumns.includes(header.title));
    }
  },
  mounted() {
    this.updateHeaders(); // Initialize headers when the component mounts
  }
}
</script>
