<template>
  <v-data-table
    :headers="headers"
    :items="items"
    :hide-default-footer="level === 0 ? false : true"
    :items-per-page="-1"
    :dense="true"
    :style="{ fontSize: fontSize }"
    :loading="loading"
    :class="{ 'grayed-out': loading }"
  >
    <template v-slot:item="{ item }">
      <tr>
        <td v-for="header in headers" :key="header.value" class="table-cell">
          <div v-if="isNested(item[header.value])">
            <RecursiveDataTable
              :data="item[header.value]"
              :level="level + 1"
              :path="[...path, header.value]"
              :nameMappingObj="nameMappingObj"
              :headdersToHide="headdersToHide"
            />
          </div>
          <a v-else-if="header.value === 'opinionUrl'" :href="item[header.value]" target="_blank">{{
            item[header.value]
          }}</a>
          <v-btn
            v-else-if="header.value.includes('djangoAdmin')"
            @click="goToDjangoAdmin(item[header.value])"
            size="x-small"
          >
            <v-icon>mdi-open-in-new</v-icon>
            go to {{ header.title.slice(0, -'Admin'.length) }}
          </v-btn>
          <div v-else>
            {{ item[header.value] }}
          </div>
        </td>
      </tr>
    </template>
  </v-data-table>
</template>

<script>
import { useMainStore } from '@/stores/main'
import { mapState } from 'pinia'

export default {
  name: 'RecursiveDataTable',
  props: {
    data: {
      type: [Object, Array],
      required: true
    },
    level: {
      type: Number,
      default: 0
    },
    loading: {
      type: Boolean,
      default: false
    },
    path: {
      type: Array,
      default: () => []
    },
    nameMappingObj: {
      type: Object,
      required: true
    },
    headdersToHide: {
      type: Array,
      default: () => []
    }
  },
  computed: {
    ...mapState(useMainStore, ['settings']),
    items() {
      if (Array.isArray(this.data)) {
        return this.data
      } else if (typeof this.data === 'object') {
        return [this.data]
      } else {
        return []
      }
    },
    headers() {
      const itemsKeys = this.items.reduce((result, obj) => {
        Object.keys(obj).forEach((key) => {
          if (!result.includes(key)) {
            result.push(key)
          }
        })
        return result
      }, [])

      return itemsKeys
        .filter((key) => !this.headdersToHide.includes(key))
        .map((key) => {
          const fullPath = [...this.path, key].join('.')
          const mappingEntry = this.nameMappingObj[fullPath]
          return {
            title: mappingEntry ? mappingEntry.displayName : key,
            value: key,
            align: 'center'
          }
        })
    },
    fontSize() {
      const baseSize = 12
      const currentSize = baseSize - this.level
      return `${currentSize < 10 ? 10 : currentSize}px`
    }
  },
  methods: {
    isNested(value) {
      return (
        value &&
        (Array.isArray(value) || (typeof value === 'object' && Object.keys(value).length > 0))
      )
    },
    goToDjangoAdmin(entityPath) {
      const backendOrigin = import.meta.env.VITE_BACKEND_ORIGIN || window.location.origin
      const url = `${backendOrigin}/${this.settings.adminPath}${entityPath}`
      window.open(url, '_blank')
    }
  }
}
</script>

<style>
.recursive-table {
  margin: 0;
  padding: 0;
}

.grayed-out {
  opacity: 0.4;
}

th {
  border-left: 0.5px solid #ccc;
  color: #557c55;
}

th:first-child {
  border-left: none;
}

td {
  text-align: center;
  vertical-align: middle;
  border-left: 0.5px solid #ccc; /* Adjust the color as needed */
}

td:first-child {
  border-left: none;
}
</style>
