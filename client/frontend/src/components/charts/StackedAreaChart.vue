<template>
  <v-chart class="chart" :option="option" autoresize />
</template>

<script setup>
import { ref, watchEffect, provide, computed } from 'vue'
import { useTheme } from 'vuetify'
import VChart, { THEME_KEY } from 'vue-echarts'
import { use } from 'echarts/core'
import {
  TitleComponent,
  ToolboxComponent,
  TooltipComponent,
  GridComponent,
  LegendComponent
} from 'echarts/components'
import { LineChart } from 'echarts/charts'
import { UniversalTransition } from 'echarts/features'
import { CanvasRenderer } from 'echarts/renderers'

use([
  TitleComponent,
  ToolboxComponent,
  TooltipComponent,
  GridComponent,
  LegendComponent,
  LineChart,
  CanvasRenderer,
  UniversalTransition
])

const option = ref({})
const appTheme = useTheme()
const chartTheme = computed(() => (appTheme.global.current.value.dark ? 'dark' : 'light'))
provide(THEME_KEY, chartTheme)

watchEffect(() => {
  updateChartOptions(chartTheme.value)
})

function updateChartOptions(theme) {
  option.value = {
    title: {
      // text: "Title of the chart",
    },
    backgroundColor: theme === 'dark' ? 'black' : null,
    tooltip: {
      trigger: 'axis',
      axisPointer: {
        type: 'cross',
        label: {
          backgroundColor: '#6a7985'
        }
      }
    },
    legend: {
      data: ['Accepted', 'Accepted with reservation', 'Rejected']
    },
    toolbox: {
      feature: {
        saveAsImage: {}
      }
    },
    grid: {
      left: '3%',
      right: '4%',
      bottom: '3%',
      containLabel: true
    },
    xAxis: [
      {
        type: 'category',
        boundaryGap: false,
        data: ['2018', '2019', '2020', '2021', '2022', '2023', '2024']
      }
    ],
    yAxis: [
      {
        type: 'value'
      }
    ],
    series: [
      {
        name: 'Accepted',
        type: 'line',
        stack: 'Total',
        emphasis: {
          focus: 'series'
        },
        data: [120, 132, 101, 134, 90, 230, 210],
        itemStyle: {
          color: '#7C9D96'
        },
        lineStyle: {
          color: '#7C9D96'
        },
        areaStyle: {
          color: 'rgba(124, 157, 150, 0.75)'
        }
      },
      {
        name: 'Accepted with reservation',
        type: 'line',
        stack: 'Total',
        emphasis: {
          focus: 'series'
        },
        data: [220, 182, 191, 234, 290, 330, 310],
        itemStyle: {
          color: '#A1CCD1'
        },
        lineStyle: {
          color: '#A1CCD1'
        },
        areaStyle: {
          color: 'rgba(161, 204, 209, 0.75)'
        }
      },
      {
        name: 'Rejected',
        type: 'line',
        stack: 'Total',
        emphasis: {
          focus: 'series'
        },
        data: [150, 232, 201, 154, 190, 330, 410],
        itemStyle: {
          color: '#E9B384'
        },
        lineStyle: {
          color: '#E9B384'
        },
        areaStyle: {
          color: 'rgba(233, 179, 132, 0.75)'
        }
      }
    ]
  }
}
</script>

<style scoped>
.chart {
  height: 30vh;
}
</style>
