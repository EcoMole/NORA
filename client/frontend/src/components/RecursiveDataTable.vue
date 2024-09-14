<template>
  <v-data-table
    :headers="headers"
    :items="items"
    :hide-default-footer="level === 0 ? false : true"
    :dense="true"
    :style="{ fontSize: fontSize }"
    :loading="loading"
    :class="{ 'grayed-out': loading }"
  >
    <template v-slot:item="{ item }">
      <tr>
        <td v-for="header in headers" :key="header.value" class="table-cell">
          <div v-if="isNested(item[header.value])">
            <RecursiveDataTable :data="item[header.value]" :level="level + 1" />
          </div>
          <div v-else>
            {{ item[header.value] }}
          </div>
        </td>
      </tr>
    </template>
  </v-data-table>
</template>

<script>
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
    }
  },
  computed: {
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
      const dataItem = this.items[0]
      if (!dataItem || typeof dataItem !== 'object') {
        return []
      }
      return Object.keys(dataItem)
        .filter((key) => key !== '__typename' && key !== 'id')
        .map((key) => ({
          title: key,
          value: key,
          align: 'center'
        }))
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
