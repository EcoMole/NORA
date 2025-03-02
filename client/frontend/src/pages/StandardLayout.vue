<template>
  <v-app-bar app fixed color="primary">
    <v-app-bar-title class="app-bar-title">NOvel food Risk Assessment (NORA)</v-app-bar-title>

    <v-spacer></v-spacer>

    <v-btn v-if="settings.adminPath" class="mr-1" color="secondary" icon @click="goToDjangoAdmin">
      <v-icon size="large">mdi-database-cog </v-icon>
      <v-tooltip activator="parent" location="bottom">Django Admin</v-tooltip>
    </v-btn>

    <v-menu v-model="menuSettings" :close-on-content-click="false">
      <template v-slot:activator="{ props }">
        <v-btn icon v-bind="props" color="secondary" class="mr-3">
          <v-icon size="large">mdi-cog</v-icon>
        </v-btn>
      </template>
      <v-list>
        <v-list-item>
          <v-switch
            hide-details
            class="ml-3"
            v-model="darkTheme"
            label="Dark theme"
            @click="toggleTheme"
          ></v-switch>
        </v-list-item>
      </v-list>
    </v-menu>
    <v-menu v-model="menuAccount" min-width="200px" :close-on-content-click="false">
      <template v-slot:activator="{ props }">
        <v-btn icon v-bind="props" class="mr-5">
          <v-avatar color="tertiary" size="large">
            <span class="text-h5">
              {{ initials }}
            </span>
          </v-avatar>
        </v-btn>
      </template>
      <v-card>
        <v-card-text>
          <div class="mx-auto text-center">
            <v-avatar color="tertiary">
              <span class="text-h5">
                {{ initials }}
              </span>
            </v-avatar>
            <p class="text-caption mt-1">
              {{ email }}
            </p>
            <v-divider class="my-3"></v-divider>
            <v-btn
              variant="text"
              color="secondary"
              @click="menuAccount = false"
              :to="{ name: 'user-page' }"
            >
              Account
            </v-btn>
            <v-divider class="my-3"></v-divider>
            <v-btn variant="text" color="tertiary" @click="doLogOut"> Log out </v-btn>
          </div>
        </v-card-text>
      </v-card>
    </v-menu>
  </v-app-bar>
  <v-navigation-drawer v-model="drawer" :rail="rail" permanent color="secondary">
    <v-list-item nav class="pl-1">
      <template v-slot:append>
        <v-btn variant="text" icon="mdi-menu" color="primary" @click.stop="rail = !rail"></v-btn>
      </template>
    </v-list-item>

    <v-divider></v-divider>

    <v-list density="compact" nav>
      <v-list-item
        :value="item.value"
        :active="$route.name === item.routerLink"
        :prepend-icon="item.icon"
        :title="item.title"
        v-for="(item, index) in drawerItems"
        :key="index"
        :to="{ name: item.routerLink }"
        color="tertiary"
        base-color="primary"
      >
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
  <v-main>
    <v-container :class="{ 'xs12 sm10 md8 lg6 xl4': true }" fluid>
      <router-view :key="$route.fullPath" />
    </v-container>
  </v-main>
</template>

<script>
import { useTheme } from 'vuetify'
import { useMainStore } from '@/stores/main'
import { mapActions, mapState } from 'pinia'
import { getInitials } from '@/libs/utils'

export default {
  data() {
    return {
      drawer: true,
      rail: true,
      fav: true,
      menuSettings: false,
      menuAccount: false,
      darkTheme: false,
      hints: true,
      drawerItems: [
        {
          title: 'Database Search',
          icon: 'mdi-database',
          value: 'databaseSearch',
          routerLink: 'database-search-page'
        },
        {
          title: 'User',
          icon: 'mdi-account',
          value: 'user',
          routerLink: 'user-page'
        }
      ]
    }
  },
  created() {
    this.theme = useTheme()
  },
  methods: {
    ...mapActions(useMainStore, ['logOut']),
    toggleTheme() {
      this.theme.global.name.value = this.theme.global.current.value.dark
        ? 'lightTheme'
        : 'darkTheme'
    },
    doLogOut() {
      this.logOut()
      this.menuAccount = false
    },
    goToDjangoAdmin() {
      const backendOrigin = import.meta.env.VITE_BACKEND_ORIGIN || window.location.origin
      const url = `${backendOrigin}/${this.settings.adminPath}`
      window.open(url, '_blank')
    }
  },
  computed: {
    ...mapState(useMainStore, ['user', 'settings']),
    initials() {
      return getInitials(this.user.firstName, this.user.lastName)
    },
    email() {
      return this.user.email || ''
    }
  }
}
</script>

<style>
.app-bar-title {
  color: #557c55;
}
</style>
