<template>
  <div class="h-screen flex flex-col  content-center items-center bg-gray-100 p-4">

    <div class="flex justify-center m-4">
      <Dropdown />
    </div>
    <div >
      <Graph class="h-[500px]" />
    </div>
  </div>
</template>

<script setup lang="ts">
import Dropdown from "./Dropdown.vue";
import Graph from "./Graph.vue";

</script>

<style scoped></style>
