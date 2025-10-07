<template>
    <Line style="height: 500px;" v-if="data" :data="data" :options="options" />
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
  Legend,
  scales,
  Ticks
} from 'chart.js'
import { Line } from 'vue-chartjs'
import type { SeriesData } from './SeriesData.ts'
import type { DataSet } from './DataSet.ts'

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
const loadedData = ref<SeriesData[]>([])
const dataSets = ref<DataSet[]>([])

onMounted(async () => {
  const res = await fetch('/index.json')
  const fileList: string[] = await res.json()

  for (const file of fileList.slice(0, 5)) {
    const res = await fetch(`/${file}`)
    const json = await res.json()

    loadedData.value.push({
      series_id: json.series_id,
      title: json.title,
      data: json.data
    })
  }

  const labels = Array.from({ length: 60 }, (_, i) =>
  new Date(new Date().setMonth(new Date().getMonth() - 59 + i))
    .toISOString()
    .slice(0, 7)
  )


  data.value = {
  labels,
  datasets: loadedData.value.map((series) => {
    const labelSet = new Set(labels)
    const filtered = series.data.filter((d: any) => labelSet.has(d.date.substring(0, 7)))
    const color = '#' + Math.floor(Math.random() * 16777215).toString(16)

    return {
      label: series.title,
      data: labels.map(label => {
        const match = filtered.find((d: any) => d.date.substring(0, 7) === label)
        return match ? match.value : null
      }),
      borderColor: color,
      backgroundColor: color,
      fill: false,
      tension: 0.1
    }
  })
}
})

const options = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    y: {
      beginAtZero: false,
      ticks: {
        stepSize: 5
      },
    }
  }
}

</script>