<template>
  <div class="h-screen flex flex-col  content-center items-center bg-gray-100 p-4">
    <div class="flex justify-center m-4">
      <Dropdown />
    </div>
    <div class="flex justify-center m-4">
      <SearchBox class="w-[500px]" />
    </div>
    <div >
      <Graph class="h-[500px]" />
    </div>
  </div>
</template>

<script setup lang="ts">
import Dropdown from "./Dropdown.vue";
import Graph from "./Graph.vue";
import SearchBox from "./SearchBox.vue";

</script>

<style scoped></style>
