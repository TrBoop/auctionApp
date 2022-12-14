<script setup lang="ts">
import Navbar from './components/Navbar.vue'
import Home from './components/Home.vue'
import Profile from './components/Profile.vue'
import Login from './components/Login.vue'
</script>

<template>
<Navbar/>

<router-view :key="$route.path" />

</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
