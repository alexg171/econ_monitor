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
import { SeriesData } from './SeriesData'

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

const allSeriesData = ref<SeriesData[]>([])

onMounted(async () => {
  const res = await fetch('/index.json')
  const fileList: string[] = await res.json()

  for (const file of fileList) {
    const res = await fetch(`/${file}`)
    const json = await res.json()

    allSeriesData.value.push({
      series_id: json.series_id,
      title: json.title,
      data: json.data
    })
  }


  const firstSeries = allSeriesData.value[0]
  if (firstSeries && Array.isArray(firstSeries.data)) {
    const labels = firstSeries.data.map((d: any) => d.date.substring(0, 7))
    const values = firstSeries.data.map((d: any) => d.value)

    data.value = {
      labels,
      datasets: [
        {
          label: firstSeries.title,
          backgroundColor: '#f87979',
          data: values,
        }
      ]
    }
  } else {
    console.warn("firstSeries or its data is undefined:", firstSeries)
  }

})

const options = {
  responsive: true,
  maintainAspectRatio: false,
  scales: {
    y: {
      ticks: {
        stepSize: 5
      }
    }
  }
}

</script>