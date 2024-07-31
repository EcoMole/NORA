import '@/assets/main.css'

import { createApp } from 'vue'
import App from '@/App.vue'
import { setupStore } from '@/stores'
import router from '@/router'
import vuetify from '@/plugins/vuetify'
import { ApolloClients } from '@vue/apollo-composable'
import client from '@/libs/apollo-client'

const app = createApp(App)

// Provide Apollo Client
app.provide(ApolloClients, {
  default: client // Provide the Apollo Client instance as the default client
})

// Setup store
setupStore(app)

// Use Vuetify
app.use(vuetify)

// Use Vue Router
app.use(router)

// Mount the app
app.mount('#app')
