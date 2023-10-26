<script setup>
console.log("About page has been loaded!");
import Sidebar from '../components/Sidebar.vue';
</script>


<template>
  <Sidebar></Sidebar>
  <div class="about bg-gray-800">
    <h1 class="title">This is an about page</h1>
    test
  </div>
</template>

<style>
@media (min-width: 1024px) {
  .about {
    min-height: 100vh;
    display: flex;
    align-items: center;
  }
}
.title {
  justify-content: center;
}
</style>

