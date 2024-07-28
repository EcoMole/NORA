<template>
  <v-col cols="4">
      <v-row class="d-flex justify-center mt-2 mb-6">
        <v-btn @click="handleClick" color="primary">Search</v-btn>
      </v-row>
      <v-row class="mt-2">
        <v-text-field label="Search filters" solo flat max-width="360"></v-text-field>
      </v-row>

      <v-row class="mt-2">
        <v-sheet elevation="1" class="pa-4" width="360">
          <v-row class="pa-2">
            <v-switch color="secondary" class="mr-4"></v-switch>
            <v-checkbox label="Attribute"></v-checkbox>
          </v-row>
        </v-sheet>
      </v-row>

      <v-row class="mt-2">
        <v-sheet elevation="1" class="pa-4" width="360">
          <v-row class="pa-2">
            <v-switch color="secondary" class="mr-5"></v-switch>
            <v-text-field label="Attribute" solo flat></v-text-field>
          </v-row>
        </v-sheet>
      </v-row>

      <v-row class="mt-2">
        <v-sheet elevation="1" class="pa-4">
          <v-switch
            color="secondary"
            label="Opinion published after date"
            class="mb-negative"
          ></v-switch>
          <v-date-picker hide-header solo flat></v-date-picker>
        </v-sheet>
      </v-row>

      <v-row class="mt-2">
        <v-sheet elevation="1" class="pa-4">
          <v-switch
            color="secondary"
            label="Opinion published before date"
            class="mb-negative"
          ></v-switch>
          <v-date-picker dense hide-header solo flat></v-date-picker>
        </v-sheet>
      </v-row>
    </v-col>
</template>
<script>
export default {
  methods: {
    handleClick() {
      this.$emit('button-clicked');
    }
  }
}
</script>
