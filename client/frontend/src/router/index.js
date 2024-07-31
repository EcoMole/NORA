import { createRouter, createWebHistory } from 'vue-router'

export default new createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/reset-your-password-here/',
      name: 'password-reset-page',
      component: () => import('@/pages/ResetPasswordPage.vue'),
      meta: { isPublic: true }
    },
    {
      path: '/',
      name: 'home-page',
      redirect: { name: 'dashboard-page' }
    },
    {
      path: '/dashboard/',
      name: 'dashboard-page',
      component: () => import('@/pages/DashboardPage.vue')
    },
    {
      path: '/graphql/',
      name: 'graphql-page',
      component: () => import('@/pages/GraphqlPage.vue')
    },
    {
      path: '/opinions/',
      name: 'opinions-page',
      component: () => import('@/pages/OpinionsPage.vue')
    },
    {
      path: '/novle-foods/',
      name: 'novel-foods-page',
      component: () => import('@/pages/NovelFoodsPage.vue')
    },
    {
      path: '/organisms/',
      name: 'organisms-page',
      component: () => import('@/pages/OrganismsPage.vue')
    },
    {
      path: '/chemicals/',
      name: 'chemicals-page',
      component: () => import('@/pages/ChemicalsPage.vue')
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
