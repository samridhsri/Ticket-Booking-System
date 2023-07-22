<template>
  <div class="home">
    <div class="d-flex justify-content-around mt-4">
      <div>
        <h3 class="text-sm-left">Hey {{ username }}! Welcome to your Dashboard</h3>
      <h5>Take a look at all the shows</h5>

      </div>
      <div>
        <input type="text" class="form-control" placeholder="Search for a show" aria-label="Search for a show" @keyup.enter="searchShow(searchForShow)" v-model="searchForShow" aria-describedby="button-addon2">
      </div>
      <div>
        <Button class="btn btn-primary" @click="seeBookings()">See All your bookings</Button>
      </div>
      
    </div>
    
    <UserDashboard/>
  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
.home {
  font-family: 'Poppins', sans-serif;
  font-size: 1.5rem;
  font-weight: 400 !important;
  letter-spacing: -1px;
  
  
}
</style>

<script>
// @ is an alias to /src

import UserDashboard from '@/components/UserDashboard.vue';

export default {
  name: 'HomeView',
  components: {
    UserDashboard,
  },
  data: function() {
    return{
      username: localStorage.getItem('email').substring(0, localStorage.getItem('email').indexOf("@")),
      searchForShow: ''
    }
  },
  methods:{
    seeBookings(){
      this.$router.push({name: 'seeTickets',params: { username: this.username}});
    },
    searchShow(showName){
      console.log(showName);
      this.$router.push({name: 'searchShow',params: { showName: showName}});
    }
  }
}
</script>
