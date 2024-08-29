import '@/assets/main.css'

import { createApp } from 'vue'
import App from '@/App.vue'
import { setupStore } from '@/stores'
import router from '@/router'
import vuetify from '@/plugins/vuetify'
// for Option API apollo provider
import { createApolloProvider } from '@vue/apollo-option'
// for Composition API apollo provider
// import { ApolloClients } from '@vue/apollo-composable'
import client from '@/libs/apollo-client'

const app = createApp(App)

// for Composition API apollo provider
// app.provide(ApolloClients, {
//   default: client // Provide the Apollo Client instance as the default client
// })


// for Option API apollo provider
const apolloProvider = createApolloProvider({
  defaultClient: client // Provide the Apollo Client instance as the default client
})
app.use(apolloProvider)
//

// Setup store
setupStore(app)

// Use Vuetify
app.use(vuetify)

// Use Vue Router
app.use(router)

// Mount the app
app.mount('#app')
