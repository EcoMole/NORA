<template>
  <v-row>
    <v-sheet
      elevation="2"
      max-width="600"
      rounded="lg"
      width="100%"
      class="pa-4 text-center mx-auto mt-10"
    >
      <UserForm
        v-if="editing === 'profile'"
        :user="mainStore.user"
        @cancel="editing = ''"
        @submit="editing = ''"
      />
      <PasswordForm
        v-else-if="editing === 'password'"
        :user="mainStore.user"
        @cancel="editing = ''"
        @submit="editing = ''"
      />
      <UserProfile v-else :user="mainStore.user" @edit="(p) => (editing = p)" />
    </v-sheet>
  </v-row>
</template>
<script setup>
import { useMainStore } from '@/stores/main'
import { ref } from 'vue'
import UserProfile from '@/components/UserProfile.vue'
import UserForm from '@/components/UserForm.vue'
import PasswordForm from '@/components/PasswordForm.vue'

const editing = ref('')
const mainStore = useMainStore()
</script>
<style>
.name {
  color: #557c55;
}
.email {
  color: #fa7070;
}
</style>
