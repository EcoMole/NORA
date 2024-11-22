<template>
  <v-main class="d-flex flex-column align-center">
    <h1 class="mt-8 mb-6 text-secondary">NOvel food Risk Assessment (NORA)</h1>
    <v-card width="450">
      <v-card-text>
        <LoginUser />
      </v-card-text>
    </v-card>
    <!-- for possible future implementation of new user creation and password resetting through the frontend -->
    <!-- <v-card width="450">
      <v-tabs v-model="tab" color="secondary" bg-color="primary">
        <v-tab value="register">Register</v-tab>
        <v-tab value="login">Log in</v-tab>
        <v-tab v-if="tab === 'reset-password'" value="reset-password">reset password</v-tab>
      </v-tabs>
      <v-card-text>
        <v-window v-model="tab">
          <v-window-item value="register">
            <RegisterUser />
          </v-window-item>
          <v-window-item value="login">
            <LoginUser @reset-password="tab = 'reset-password'" />
          </v-window-item>
          <v-window-item value="reset-password">
            <RequestResetPassword @cancel="tab = 'login'" />
          </v-window-item>
        </v-window>
      </v-card-text>
    </v-card> -->
  </v-main>
</template>

<script>
import LoginUser from '@/components/LoginUser.vue'
// import RegisterUser from '@/components/RegisterUser.vue'
// import RequestResetPassword from '@/components/RequestResetPassword.vue'

export default {
  components: { LoginUser }, // RegisterUser, RequestResetPassword
  data: () => ({}),
  methods: {}
}
</script>

<style scoped>
.v-slide-group__content {
  color: green !important;
}
</style>
