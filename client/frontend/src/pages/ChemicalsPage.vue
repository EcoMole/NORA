<template>
  <h1>Chemical Identities</h1>
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
            :items="['Name', 'Synonym', 'CAS number', 'Molecular Formula']"
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
              :items="chemicals"
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
      dateImput: null,
      showInColumns: ["Name"],
      showInDetails: [],
      sortBy: [{ key: 'calories', order: 'asc' }],
      headers: [],
      chemicals: [
        {
          name: 'Water',
          synonym: 'Dihydrogen Oxide',
          cas_number: '7732-18-5',
          molecular_formula: 'H2O'
        },
        {
          name: 'Sodium Chloride',
          synonym: 'Table Salt',
          cas_number: '7647-14-5',
          molecular_formula: 'NaCl'
        },
        {
          name: 'Ethanol',
          synonym: 'Alcohol',
          cas_number: '64-17-5',
          molecular_formula: 'C2H6O'
        },
        {
          name: 'Acetic Acid',
          synonym: 'Vinegar',
          cas_number: '64-19-7',
          molecular_formula: 'C2H4O2'
        },
        {
          name: 'Sucrose',
          synonym: 'Table Sugar',
          cas_number: '57-50-1',
          molecular_formula: 'C12H22O11'
        },
        {
          name: 'Carbon Dioxide',
          synonym: 'Dry Ice',
          cas_number: '124-38-9',
          molecular_formula: 'CO2'
        },
        {
          name: 'Ammonia',
          synonym: 'NH3',
          cas_number: '7664-41-7',
          molecular_formula: 'NH3'
        },
        {
          name: 'Calcium Carbonate',
          synonym: 'Chalk',
          cas_number: '471-34-1',
          molecular_formula: 'CaCO3'
        },
        {
          name: 'Silicon Dioxide',
          synonym: 'Quartz',
          cas_number: '7631-86-9',
          molecular_formula: 'SiO2'
        },
        {
          name: 'Methane',
          synonym: 'Marsh Gas',
          cas_number: '74-82-8',
          molecular_formula: 'CH4'
        }
      ]
    }
  },
  methods: {
    updateHeaders() {
      const allHeaders = [
        { title: 'Name', key: 'name' },
        { title: 'Synonym', key: 'synonym' },
        { title: 'CAS number', key: 'cas_number' },
        { title: 'Molecular Formula', key: 'molecular_formula' }
      ]
      this.headers = allHeaders.filter((header) => this.showInColumns.includes(header.title))
    }
  },
  mounted() {
    this.updateHeaders()
  }
}
</script>
