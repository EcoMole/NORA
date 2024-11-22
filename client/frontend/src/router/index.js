import { createRouter, createWebHistory } from 'vue-router'

export default new createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      // for possible future implementation of new user creation and password resetting through the frontend
      path: '/reset-your-password-here/',
      name: 'password-reset-page',
      component: () => import('@/pages/ResetPasswordPage.vue'),
      meta: { isPublic: true }
    },
    {
      path: '/',
      name: 'home-page',
      redirect: { name: 'database-search-page' }
    },
    {
      path: '/database-search/',
      name: 'database-search-page',
      component: () => import('@/pages/DatabaseSearchPage.vue')
    },
    {
      path: '/user/',
      name: 'user-page',
      component: () => import('@/pages/UserPage.vue')
    },
    {
      path: '/settings/',
      name: 'settings-page',
      component: () => import('@/pages/SettingsPage.vue')
    }
  ]
})
