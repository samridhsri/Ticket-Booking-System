<template>
    <div class="">
    <div class="container p-5 m-5 h-auto border border-5 rounded-5 " v-for="venue in venues">
        <h1 class="">{{ venue[1] }}</h1>
        <div class="row col-lg-12 px-5 mx-auto mb-4">
        <div class="card mx-auto" style="width: 18rem;" v-for="show in venueAndShows[venue[1]]">
            <div class="card-body">
                <div class="">
                    <h5 class="card-title">{{ show[1] }}</h5>
                    <h6 class="card-subtitle mb-2 text-body-secondary">time: {{show[3]}}</h6>
                </div>

                <button type="button" class="btn btn-primary mt-3" @click="bookTicket(show[1],venue[1],username)">Book Ticket</button>
            </div>
        </div>
    </div>
    </div>
</div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
.bg-custom {
  
}
</style>

<script>
import axios from 'axios';

export default {
    name: 'UserDashboard',
    data() {
        return {
            username: localStorage.getItem('email').substring(0, localStorage.getItem('email').indexOf("@")),
            email: localStorage.getItem('email'),
            venues: ['Venue 1', 'Venue 2', 'Venue 3'],
            shows: ['Show 1', 'Show 2', 'Show 3'],
            venueAndShows: {}
        }
    },
    methods: {
        bookTicket(showname, venuename, username){
            console.log('book ticket');
            this.$router.push({name: 'bookTicket',params: { username: username, venuename: venuename, showname: showname }});
            
        }
        
    },
    created(){
        axios.get('http://127.0.0.1:5000/api/all-details')
      .then(response => {
        console.log(response.data);
        this.venues = response.data.venueList;
        this.shows = response.data.showList;
        this.venueAndShows = response.data.venueAndShow;
      })
      .catch(error => {
        console.log(error);
      });

    //   axios.get('http://127.0.0.1:5000/api/show-details').then(
    //     response => {
    //         console.log(response.data);
    //     }
    //   ).catch(error=>{
    //       console.log(error);
    //     }
    //   );
    }
}
</script>