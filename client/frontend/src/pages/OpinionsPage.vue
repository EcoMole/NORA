<template>
  <div>
    <h1>Opinions</h1>
  </div>

  <v-row class="ma-3 justify-center">
    <v-text-field
      v-model="search"
      clearable
      density="comfortable"
      hide-details
      placeholder="Novel Food title"
      prepend-inner-icon="mdi-magnify"
      style="max-width: 300px"
      variant="solo"
    ></v-text-field>
  </v-row>

  <div>
    <v-data-iterator item-value="id" :items="novelFoods" :items-per-page="4" :search="search">
      <template v-slot:default="{ items, isExpanded, toggleExpand }">
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
                <tbody>
                  <tr align="right">
                    <th>NF Code:</th>
                    <td>${{ item.raw.NFcode }}</td>
                  </tr>
                  <tr align="right">
                    <th>DOI:</th>
                    <td>{{ item.raw.doi }}</td>
                  </tr>
                  <tr align="right">
                    <th>Question number:</th>
                    <td>{{ item.raw.questionNo }}</td>
                  </tr>
                  <tr align="right">
                    <th>Date of publication:</th>
                    <td>{{ item.raw.published }}</td>
                  </tr>
                </tbody>
              </v-table>
              <div class="px-4">
                <v-switch
                  :model-value="isExpanded(item)"
                  :label="`${isExpanded(item) ? 'Hide' : 'Show'} details`"
                  density="compact"
                  inset
                  @click="() => toggleExpand(item)"
                ></v-switch>
                <v-divider></v-divider>
                <v-expand-transition>
                  <div v-if="isExpanded(item)">
                    <v-card-text>
                      A lot more information about the {{ item.raw.title }}: Lorem ipsum dolor sit
                      amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore
                      et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation
                      ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor
                      in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla
                      pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui
                      officia deserunt mollit anim id est laborum.
                    </v-card-text>
                  </div>
                </v-expand-transition>
              </div>
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
    search: '',
    expandedItems: {},
    novelFoods: [
      {
        id: 1,
        NFcode: 'ad183d1-4732',
        title: 'yellow/orange tomato extract',
        subtitle: 'some subtitle about the yellow/orange tomato extract',
        doi: 'https://doi.org/10.2903/j.efsa.2023.77894',
        questionNo: 'EFSA‐Q‐2021‐001',
        published: '2023/08/06'
      },
      {
        id: 2,
        NFcode: '18a31-4732',
        title: 'Isomalto-oligosaccharide',
        subtitle: 'some subtitle about the Isomalto-oligosaccharide',
        doi: 'https://doi.org/10.2903/j.efsa.2023.787294',
        questionNo: 'EFSA‐Q‐2018‐00201',
        published: '2023/12/07'
      },
      {
        id: 3,
        NFcode: '5adf-818',
        title: 'Isomalto-oligosaccharide',
        subtitle: 'some subtitle about the Isomalto-oligosaccharide',
        doi: 'https://doi.org/10.2903/j.efsa.2021.8989',
        questionNo: 'EFSA‐Q‐2021‐18601',
        published: '2021/12/07'
      },
      {
        id: 4,
        NFcode: 'a1df83df1-4fds732',
        title: '2’-Fucosyllactose (2’-FL)',
        subtitle: 'some subtitle about the 2’-Fucosyllactose (2’-FL)',
        doi: 'https://doi.org/10.2903/j.efsa.2023.728794',
        questionNo: 'EFSA‐Q‐2021‐7201',
        published: '2023/03/06'
      },
      {
        id: 5,
        NFcode: '1448sf31-47f3s2',
        title: 'Pelargonium sidoides',
        subtitle: 'some subtitle about the Pelargonium sidoides',
        doi: 'https://doi.org/10.2903/j.efsa.2023.28794',
        questionNo: 'EFSA‐Q‐2022‐40201',
        published: '2023/10/16'
      },
      {
        id: 6,
        NFcode: '14411-4732',
        title: 'Ashitaba sap powder',
        subtitle: 'some subtitle about the Ashitaba sap powder',
        doi: 'https://doi.org/10.2903/j.efsa.2023.72794',
        questionNo: 'EFSA‐Q‐2031‐88201',
        published: '2023/01/06'
      },
      {
        id: 7,
        NFcode: '8481-4732',
        title: 'Synthetic paraxanthine',
        subtitle: 'some subtitle about the Synthetic paraxanthine',
        doi: 'https://doi.org/10.2903/j.efsa.2023.989794',
        questionNo: 'EFSA‐Q‐2020‐70201',
        published: '2023/10/02'
      }
    ]
  })
}
</script>
