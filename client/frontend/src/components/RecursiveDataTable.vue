<template>
  <v-data-table
    :headers="headers"
    :items="data"
    :hide-default-footer="hideFooter(data)"
    :items-per-page="10"
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
              :data="toArray(item[header.value])"
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
            {{ displayValue(item[header.value]) }}
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
      type: [Array],
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
    headers() {
      const dataItem = this.data[0]
      if (!dataItem || typeof dataItem !== 'object') {
        return []
      }
      return Object.keys(dataItem)
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
    toArray(value) {
      return Array.isArray(value) ? value : [value]
    },
    isNested(value) {
      // returns true if the value is non-empty object or non-empty array and is not a Date
      return (
        value &&
        typeof value == 'object' &&
        Object.keys(value).length > 0 &&
        !(value instanceof Date)
      )
    },
    hideFooter(value) {
      // footer will be shown for level 0 table and for recursive tables with more than 10 rows
      if (this.level === 0) {
        return false
      }
      if (!value || value instanceof Date) {
        return true
      }
      if (Array.isArray(value) && value.length < 11) {
        return true
      }
      return false
    },
    goToDjangoAdmin(entityPath) {
      const backendOrigin = import.meta.env.VITE_BACKEND_ORIGIN || window.location.origin
      const url = `${backendOrigin}/${this.settings.adminPath}${entityPath}`
      window.open(url, '_blank')
    },
    displayValue(value) {
      // Check for null, empty array, or empty object
      if (value === null || (typeof value === 'object' && Object.keys(value).length === 0)) {
        return '-'
      }
      return value
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
