<template>
  <div>
    <h1>Novel Foods</h1>
    <v-btn @click="loadNovelFoods">Load Data</v-btn>
    <ul v-if="novelFoodsData">
      <li v-for="item in novelFoodsData.novelFoods" :key="item.id">{{ item.title }} ({{ item.nfCode }})</li>
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
import gql from 'graphql-tag';
import { ref } from 'vue';
import { useApolloClient } from '@vue/apollo-composable';

export default {
  setup() {
    const novelFoodsData = ref(null);
    const opinionsData = ref(null);
    const loading = ref(false);
    const error = ref(null);

    const { client } = useApolloClient();

    const GET_NOVEL_FOODS = gql`
      query {
        novelFoods {
          id
          title
          nfCode
        }
      }
    `;

    const GET_OPINIONS = gql`
      query {
        opinions {
          id
          url
          doi
        }
      }
    `;

    const loadNovelFoods = async () => {
      loading.value = true;
      try {
        const result = await client.query({
          query: GET_NOVEL_FOODS
        });
        novelFoodsData.value = result.data;
      } catch (err) {
        error.value = err;
      } finally {
        loading.value = false;
      }
    };

    const loadOpinions = async () => {
      loading.value = true;
      try {
        const result = await client.query({
          query: GET_OPINIONS
        });
        opinionsData.value = result.data;
      } catch (err) {
        error.value = err;
      } finally {
        loading.value = false;
      }
    };

    return {
      novelFoodsData,
      opinionsData,
      loading,
      error,
      loadNovelFoods,
      loadOpinions
    };
  }
}
</script>
