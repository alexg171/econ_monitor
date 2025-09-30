<template>
  <Line v-if="data" :data="data" :options="options" />
</template>


<script lang="ts" setup>
import { onMounted, ref } from 'vue'
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
} from 'chart.js'
import { Line } from 'vue-chartjs'

ChartJS.register(
  CategoryScale,
  LinearScale,
  PointElement,
  LineElement,
  Title,
  Tooltip,
  Legend
)

const data = ref()

onMounted(async () => {
  const res = await fetch('/cpi_series.json')
  const json = await res.json()

  const labels = json.map((d: any) => d.date.substring(0, 7))
  const values = json.map((d: any) => d.value)

  data.value = {
    labels,
    datasets: [
      {
        label: 'CPI',
        backgroundColor: '#f87979',
        data: values,
      }
    ]
  }
})

const options = {
  responsive: true,
  maintainAspectRatio: false
}

</script>