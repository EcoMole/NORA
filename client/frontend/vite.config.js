import { fileURLToPath, URL } from 'node:url'
import vuetify from 'vite-plugin-vuetify'
import { defineConfig, loadEnv } from 'vite'
import vue from '@vitejs/plugin-vue'
/* eslint-disable */
export default defineConfig(({ command, mode }) => {
  // Get the correct env file based on the mode
  const env = loadEnv(mode, process.cwd())

  // Use the environment variable
  const URLBase = env.VITE_API_URL
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
      define: {
        'process.env.VITE_API_URL': JSON.stringify(URLBase)
      },
      server: {
        proxy: {
          '/api/': {
            target: URLBase,
            changeOrigin: true,
            ws: true
          },
          '/static/': {
            target: URLBase,
            changeOrigin: true,
            ws: true
          },
          '/media/': {
            target: URLBase,
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
