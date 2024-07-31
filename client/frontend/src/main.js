import '@/assets/main.css'

import { createApp, provide, h } from 'vue'
import App from '@/App.vue'
import { setupStore } from '@/stores'
import router from '@/router'
import vuetify from '@/plugins/vuetify'
import { ApolloClients } from '@vue/apollo-composable'
import apolloClient from '@/libs/apollo-client'

const app = createApp({
  setup() {
    provide(ApolloClients, {
      defaultClient: apolloClient
    })
  },
  render: () => h(App)
  // function to render the main App component
})

// Setup store
setupStore(app)

// Use Vuetify
app.use(vuetify)

// Use Vue Router
app.use(router)

// Mount the app\
app.mount('#app')
