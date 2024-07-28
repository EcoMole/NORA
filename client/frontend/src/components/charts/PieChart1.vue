<template>
  <v-chart class="chart" :option="option" autoresize />
</template>

<script setup>
import { ref, watchEffect, provide, computed } from 'vue'
import { use } from 'echarts/core'
import { CanvasRenderer } from 'echarts/renderers'
import { PieChart } from 'echarts/charts'
import { TooltipComponent, LegendComponent } from 'echarts/components'
import VChart, { THEME_KEY } from 'vue-echarts'
import { useTheme } from 'vuetify'

use([CanvasRenderer, PieChart, TooltipComponent, LegendComponent])

const option = ref({})
const appTheme = useTheme()
const chartTheme = computed(() => (appTheme.global.current.value.dark ? 'dark' : 'light'))
provide(THEME_KEY, chartTheme)

watchEffect(() => {
  updateChartOptions(chartTheme.value)
})

function updateChartOptions(theme) {
  option.value = {
    tooltip: {
      trigger: 'item',
      formatter: '{a} <br/>{b} : {c} ({d}%)'
    },
    backgroundColor: theme === 'dark' ? 'black' : null,
    legend: {
      orient: 'vertical',
      left: 'left'
    },
    series: [
      {
        name: 'Questions',
        type: 'pie',
        radius: '70%',
        center: ['60%', '40%'],
        data: [
          { value: 385, name: 'Assessed' },
          { value: 100, name: 'In progress' },
          { value: 234, name: 'Waiting' }
        ],
        color: [
          '#FFF8E3', // Color for 'Assessed'
          '#F3D7CA', // Color for 'In progress'
          '#E6A4B4' // Color for 'Waiting'
        ],
        emphasis: {
          itemStyle: {
            shadowBlur: 10,
            shadowOffsetX: 0,
            shadowColor: 'rgba(0, 0, 0, 0.5)'
          }
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
