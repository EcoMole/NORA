import { createVuetify } from 'vuetify'
import 'vuetify/styles'
import { md3 } from 'vuetify/blueprints'
import '@mdi/font/css/materialdesignicons.css'

// I am using components autoimporting plugin vite-plugin-vuetify, if doesnt work use conventional importing all components https://vuetifyjs.com/en/getting-started/installation/#manual-steps

const lightTheme = {
  dark: false,
  colors: {
    background: '#F2FFE9',
    surface: '#FFFFFF',
    primary: '#A6CF98',
    secondary: '#557C55',
    tertiary: '#FA7070',
    error: '#B00020',
    info: '#2196F3',
    success: '#4CAF50',
    warning: '#FB8C00'
    // anchor: "#F6C667",
  }
}

const darkTheme = {
  dark: true,
  colors: {
    primary: '#A6CF98',
    secondary: '#557C55',
    tertiary: '#FA7070',
    // on invert background with surface:
    background: '#212121',
    surface: '#000000'
  }
}

export default createVuetify({
  blueprint: md3,
  icons: {
    defaultSet: 'mdi'
  },
  theme: {
    defaultTheme: import.meta.env.VITE_DEFAULT_THEME == 'dark' ? 'darkTheme' : 'lightTheme',
    themes: {
      lightTheme,
      darkTheme
    }
  }
})
