<template>
    <div>
    <h1>Welcome</h1>
    <div class="container border p-5" v-for="venue in venues">
        <h1 class="">{{ venue[1] }}</h1>
        <div class="row col-lg-12 px-5 mx-auto mb-4">
        <div class="card" style="width: 18rem;" v-for="show in shows">
            <div class="card-body">
                <div class="">
                    <h5 class="card-title">{{ show[1] }}</h5>
                    <h6 class="card-subtitle mb-2 text-body-secondary">time: {{show[3]}}</h6>
                </div>

                <button type="button" class="btn btn-primary mt-3">Book Ticket</button>
            </div>
        </div>
    </div>
    </div>
</div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'UserDashboard',
    data() {
        return {
            user: {
                name: 'User',
                email: ''},
            venues: ['Venue 1', 'Venue 2', 'Venue 3'],
            shows: ['Show 1', 'Show 2', 'Show 3']
        }
    },
    methods: {
        
    },
    created(){
        axios.get('http://127.0.0.1:5000/api/all-details')
      .then(response => {
        console.log(response.data);
        this.venues = response.data.venueList;
        this.shows = response.data.showList;
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