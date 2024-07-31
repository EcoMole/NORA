<template>
  <div>
    <h1>Novel Foods</h1>
    <v-btn @click="loadData">Load Data</v-btn>
    <ul v-if="data">
      <li v-for="item in data.novelFoods" :key="item.id">{{ item.title }} ({{ item.nfCode }})</li>
    </ul>
  </div>
</template>

<script>
import gql from 'graphql-tag';
import { ref } from 'vue';
import { useApolloClient } from '@vue/apollo-composable';

export default {
  setup() {
    const data = ref(null);
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

    const loadData = async () => {
      loading.value = true;
      try {
        const result = await client.query({
          query: GET_NOVEL_FOODS
        });
        data.value = result.data;
      } catch (err) {
        error.value = err;
      } finally {
        loading.value = false;
      }
    };

    return {
      data,
      loading,
      error,
      loadData
    };
  }
}
</script>
