

<template>
  <div>
    <Navbar/>
  </div>
</template>

<style>
#app {
  font-family: Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: rgb(130, 101, 167);
}
</style>

<script>
import Navbar from './components/Navbar.vue'
export default {
  components: {
    Navbar,
  },
  
}
</script>
