<template>
  <h1>Novel Foods</h1>
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
            :items="[
              'Allergenicity',
              'NF Code',
              'Novel Food Title',
              'Was Tox Study Required',
              'Has Nutri Disadvantage'
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
              'Remarks'
            ]"
          ></v-combobox>
        </v-row>
        <v-row>
          <v-sheet elevation="1" class="mt-2">
            <v-data-table
              v-model:sort-by="sortBy"
              :headers="headers"
              :items="novelFoods"
            ></v-data-table>
          </v-sheet>
        </v-row>
      </v-container>
    </v-col>
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
      showInColumns: ['NF Code'],
      headers: [],
      novelFoods: [
        {
          allergenicity: 'Low',
          nfCode: 'NF001',
          novelFoodTitle: 'Cultured Meat',
          wasToxStudyRequired: true,
          hasNutriDisadvantage: false
        },
        {
          allergenicity: 'High',
          nfCode: 'NF002',
          novelFoodTitle: 'Engineered Probiotics',
          wasToxStudyRequired: true,
          hasNutriDisadvantage: true
        },
        {
          allergenicity: 'Moderate',
          nfCode: 'NF003',
          novelFoodTitle: 'Algae-based Omega 3',
          wasToxStudyRequired: false,
          hasNutriDisadvantage: false
        },
        {
          allergenicity: 'Unknown',
          nfCode: 'NF004',
          novelFoodTitle: 'Synthetic Vanillin',
          wasToxStudyRequired: true,
          hasNutriDisadvantage: true
        }
      ]
    }
  },
  methods: {
    updateHeaders() {
      const allHeaders = [
        { text: 'Allergenicity', value: 'allergenicity' },
        { text: 'NF Code', value: 'nfCode' },
        { text: 'Novel Food Title', value: 'novelFoodTitle' },
        { text: 'Was Tox Study Required', value: 'wasToxStudyRequired' },
        { text: 'Has Nutri Disadvantage', value: 'hasNutriDisadvantage' }
      ]
      this.headers = allHeaders.filter((header) => this.showInColumns.includes(header.text))
    }
  },
  mounted() {
    this.updateHeaders()
  }
}
</script>
