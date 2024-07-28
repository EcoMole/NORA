import { fileURLToPath, URL } from 'node:url'
import vuetify from 'vite-plugin-vuetify'
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

const devURLBase = 'http://127.0.0.1:8000/'

/* eslint-disable */
export default defineConfig(({ command, mode }) => {
  /* eslint-enable */
  // base configuration: used in both development and production:
  const baseConfig = {
    plugins: [vue(), vuetify({ autoImport: true })],
    resolve: {
      alias: {
        '@': fileURLToPath(new URL('./src', import.meta.url))
      }
    }
  }
  if (command === 'serve') {
    // development configuration: base configuration extended for configuratiion used only in development
    return {
      ...baseConfig,
      server: {
        proxy: {
          '/api/': {
            target: devURLBase,
            changeOrigin: true,
            ws: true
          },
          '/static/': {
            target: devURLBase,
            changeOrigin: true,
            ws: true
          },
          '/media/': {
            target: devURLBase,
            changeOrigin: true,
            ws: true
          }
        }
        // to disable error overlay that Vue uses in development mode:
        // hmr: {
        //   overlay: process.env.BUILD == "yes" ? false : { errors: false },
        // },
      }
    }
  } else {
    return baseConfig
  }
})
