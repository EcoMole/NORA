import axios from '@/libs/axios'
import { defineStore } from 'pinia'

import errorMessageParser from '@/libs/error-message-parser'

export const useMainStore = defineStore({
  id: 'auth',
  state: () => ({
    isAuthenticated: false,
    appInitialized: false,
    user: {
      pk: null,
      username: null,
      email: null,
      firstName: null,
      lastName: null,
      isSuperuser: null,
      isStaff: null,
      extraData: null
    },
    settings: {
      adminPath: null
    },
    snackbar: {
      show: false,
      color: '',
      message: '',
      icon: '',
      timeout: 4000
    },
    offeringCompactTable: false
  }),
  getters: {},
  actions: {
    async initializeApp() {
      try {
        await this.refreshAccessToken()
        if (this.isAuthenticated) {
          this.loadData()
        }
      } finally {
        this.appInitialized = true
        this.setCsrfToken()
      }
    },
    async refreshAccessToken() {
      try {
        await axios.post('/api/v1/auth/token/refresh/')
        this.isAuthenticated = true
      } catch (error) {
        this.isAuthenticated = false
      }
    },
    async loadData() {
      this.fetchSettings()
      this.fetchUser()
    },
    async fetchSettings() {
      axios.get('/api/v1/settings/').then((response) => {
        this.settings.adminPath = response.data.django_admin_path || null
      })
    },
    async fetchUser() {
      axios
        .get('/api/v1/user/')
        .then((response) => {
          this.user.pk = response.data.pk
          this.user.username = response.data.username
          this.user.email = response.data.email
          this.user.firstName = response.data.first_name
          this.user.lastName = response.data.last_name
          this.user.isSuperuser = response.data.is_superuser
          this.user.isStaff = response.data.is_staff
          this.user.extraData = response.data.extra_data
        })
        .catch((error) => {
          if (error.response?.status == 401) {
            this.isAuthenticated = false
          }
        })
    },
    setCsrfToken() {
      axios.get('/api/v1/csrf/')
    },
    authenticate() {
      this.isAuthenticated = true
    },
    deauthenticate() {
      this.isAuthenticated = false
    },
    offerCompactTable() {
      this.offeringCompactTable = true

    },
    resetOfferingCompactTable() {
      this.offeringCompactTable = false
    },
    async logOut() {
      axios
        .post('/api/v1/auth/logout/')
        .then(() => {
          this.isAuthenticated = false
          this.handleSuccess('You have been successfully logged out.')
        })
        .catch((error) => {
          this.handleError(error.response.data)
        })
    },
    handleSuccess(successMessage) {
      Object.assign(this.snackbar, {
        message: successMessage,
        color: 'secondary',
        icon: 'mdi-check',
        show: true,
        timeout: 5000
      })
    },
    handleError(errorMessage) {
      Object.assign(this.snackbar, {
        message: errorMessageParser(errorMessage),
        color: 'tertiary',
        icon: 'mdi-exclamation',
        timeout: 12000,
        show: true
      })
    },
    closeSnackbar() {
      this.snackbar.show = false
    }
  }
})
