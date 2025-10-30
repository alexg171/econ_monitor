<template>
    <div>
        <input type="text" v-model="searchQuery" placeholder="Search series..." class="bg-gray-50 border border-gray-300 text-gray-900 text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5" />
        <div v-if="searchQuery.length > 3">
            <span>{{ filteredItems.length }} series found</span>
            <ul>
                <li v-for="item in filteredItems" :key="item.item_code">{{ item.series_title }}</li>
            </ul>
        </div>
    </div>
</template>

<script lang="ts" setup>
import { onMounted, ref, computed} from 'vue';
import type { SeriesMeta } from './SeriesMeta';

const searchQuery = ref('')
const seriesList = ref<Array<SeriesMeta>>([])
const filteredItems = computed(() => {
    return seriesList.value.filter(item => 
        item.series_title.toLowerCase().includes(searchQuery.value.toLowerCase())
    );
});

// computed: {
//     filteredItems() {
//       return this.items.filter(item => {
//          return item.type.toLowerCase().indexOf(this.search.toLowerCase()) > -1
//       })
//     }
//   }


onMounted(async () => {
    const res = await fetch('/series.json')
    seriesList.value = await res.json()
});

</script>