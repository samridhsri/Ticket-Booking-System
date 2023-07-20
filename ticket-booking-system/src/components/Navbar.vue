<template>
  <div id="app">
    <nav class="navbar navbar-expand-md bg-light">
      <div class="navbar-collapse collapse w-100 order-1 mt-1 order-md-0 dual-collapse2">
        <ul class="navbar-nav mr-auto">
          <li class="nav-item mt-1">
      <router-link class="navbar-brand" to="/">Campus Ticket Hub</router-link>
          </li>
          <li class="nav-item">
            <router-link class="nav-link" to="/">Home</router-link>
          </li>
          <li>
            <router-link class="nav-link" to="/about">About</router-link>
          </li>
          <li>
            <router-link class="nav-link" to="/login">Login</router-link>
          </li>
          <li>
            <router-link class="nav-link" to="/admin-login">Admin Login</router-link>
          </li>
        </ul>
      </div>
        
          
          <div class="ml-auto">
            <uL>
              <li class="nav-item mt-1 list-unstyled ">
            <button class="button btn-primary btn" v-if="checkLogin()" @click=logout()>Logout</button>
              </li>
            </uL>

          </div>

       
        
    </nav>
    <router-view />
  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@600&display=swap');

.nav-link {
  color: rgba(50, 6, 90, 1);
  font-family: 'Poppins', sans-serif;
}
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
    },
    checkLogin() {
      return localStorage.getItem('token') !== null;

    }
  }
}


</script>