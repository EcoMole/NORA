<template>
  <div>
    <h1>Novel Foods</h1>
    <v-btn @click="loadNovelFoods">Load Data</v-btn>
    <ul v-if="novelFoodsData">
      <li v-for="item in novelFoodsData.novelFoods" :key="item.id">
        {{ item.title }} ({{ item.nfCode }})
      </li>
    </ul>
  </div>
  <div>
    <h1>Opinions</h1>
    <v-btn @click="loadOpinions">Load Data</v-btn>
    <ul v-if="opinionsData">
      <li v-for="item in opinionsData.opinions" :key="item.id">{{ item.url }} ({{ item.doi }})</li>
    </ul>
  </div>
</template>

<script>
import gql from 'graphql-tag'
import { ref } from 'vue'
import { useApolloClient } from '@vue/apollo-composable'

export default {
  setup() {
    const novelFoodsData = ref(null)
    const opinionsData = ref(null)
    const loading = ref(false)
    const error = ref(null)

    const { client } = useApolloClient()

    const GET_NOVEL_FOODS = gql`
      query {
        novelFoods {
          id
          title
          nfCode
        }
      }
    `

    // the rest of the NovelFood attributes to include:
    // title
    // nf_code
    // tox_study_required
    // genotox_final_outcome
    // final_toxicology_remarks
    // protein_digestibility
    // antinutritional_factors
    // has_nutri_disadvantage
    // nutri_disadvantage_explanation
    // sufficient_data
    // food_matrices
    // instability_concerns
    // shelflife_value
    // shelflife_unit
    // endocrine_disrupt_prop
    // outcome
    // outcome_remarks
    // vocab_id
    // allergenicity

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

    const loadNovelFoods = async () => {
      loading.value = true
      try {
        const result = await client.query({
          query: GET_NOVEL_FOODS
        })
        novelFoodsData.value = result.data
      } catch (err) {
        error.value = err
      } finally {
        loading.value = false
      }
    }

    const loadOpinions = async () => {
      loading.value = true
      try {
        const result = await client.query({
          query: GET_ALL_DATA
        })
        opinionsData.value = result.data
        console.log(result.data)
      } catch (err) {
        error.value = err
      } finally {
        loading.value = false
      }
    }

    return {
      novelFoodsData,
      opinionsData,
      loading,
      error,
      loadNovelFoods,
      loadOpinions
    }
  }
}
</script>
