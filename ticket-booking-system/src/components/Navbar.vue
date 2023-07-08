<template>
    <div id="app">
      <nav>
        <router-link to="/">Home</router-link> |
        <router-link to="/about">About</router-link> |
        <router-link to="/login">Login</router-link> |
        <router-link to="/register">Register</router-link> |
        <button class="button btn-primary btn " @click=logout()>Logout</button>
      </nav>
      <router-view/>
    </div>
</template>

<style>
</style>

<script>

export default {
  name: 'Navbar',
  methods: {
    logout() {
      localStorage.removeItem('token');
      if (localStorage.getItem('token') === null) {
        this.$router.push('/intro');
      }
    }
  }
}


</script>