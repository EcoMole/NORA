// ApolloClient: This is the core class used to initiate a connection with a GraphQL server.
// InMemoryCache: This is a standard caching implementation provided by Apollo. It stores query results in memory for better performance.
// createHttpLink: This function helps create an HTTP link to connect your Apollo Client with your GraphQL server.
// setContext: This function is used to set the context for each request, often used to add authentication headers.
import { ApolloClient, InMemoryCache, createHttpLink } from '@apollo/client'
import { setContext } from '@apollo/client/link/context'
import Cookies from 'js-cookie'

// Creates HTTP link to your GraphQL server
// The URI is pointing to the GraphQL endpoint on the backend
const httpLink = createHttpLink({
  uri: '/api/v1/graphql/'
})

// Set up the authentication link to include the JWT token from the cookie
const authLink = setContext((_, { headers }) => {
  // Retrieve the token from the 'access-token' cookie
  const token = Cookies.get('access-token')

  // Return the headers to the context so that HTTP link can read them
  return {
    headers: {
      ...headers, // Spread the existing headers
      authorization: token ? `Bearer ${token}` : '' // Add the Authorization header if the token exists
    }
  }
})

// Create an instance of Apollo Client
const client = new ApolloClient({
  // Combine the authentication link and the HTTP link
  link: authLink.concat(httpLink), // First use authLink to set headers, then httpLink to handle the HTTP connection

  devtools: {
    enabled: true
  }, // Enable Apollo DevTools in browser

  // Use in-memory cache for better performance
  cache: new InMemoryCache() // Apollo's standard caching mechanism to store query results in memory
})

// Exports the configured Apollo Client instance so it can be imported and used the Vue.js application
export default client
