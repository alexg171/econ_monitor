<template>
    <div class="flex flex-col">
        <div>
            <fwb-autocomplete
            v-model="selectedIndicator"
            :options="seriesList"
            :search-fields="['series_title']"
            display="series_title"
            placeholder="Select an indicator"
            />
        </div>
        <div>
            <li>
                <ul v-for="(item, idx) in selectedIndicatorList" :key="idx">
                    {{ item.series_title }}
                </ul>
            </li>
        </div>
    </div>
</template>

<script lang="ts" setup>
import { onMounted, ref, watch } from 'vue';
import type { SeriesMeta } from './SeriesMeta';
import { FwbAutocomplete } from 'flowbite-vue';

const selectedIndicator = ref<SeriesMeta | null>(null)
const seriesList = ref<SeriesMeta[]>([])
const selectedIndicatorList = ref<SeriesMeta[]>([])

onMounted(async () => {
    try {
        const res = await fetch('/series.json')
        seriesList.value = (await res.json()) ?? []
    } catch (e) {
        console.error('Failed to load series list', e)
        seriesList.value = []
    }
});

watch(selectedIndicator, (newVal, oldVal) => {
    if (newVal !== null) {
        selectedIndicatorList.value.push(newVal);
    }
})

</script>