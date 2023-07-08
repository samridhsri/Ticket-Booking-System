<template>
  <div class="home">


    <h1>You are here means you are verified</h1>
    <UserDashboard/>
  </div>
</template>

<script>
// @ is an alias to /src

import UserDashboard from '@/components/UserDashboard.vue';

export default {
  name: 'HomeView',
  components: {
    UserDashboard
  }
}
</script>
