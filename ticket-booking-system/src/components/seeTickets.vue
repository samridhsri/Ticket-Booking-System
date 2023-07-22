<template>
    <div class="seeTickets">
      <div class="text-align-custom">
            <h1 class="">Your Bookings</h1>
        </div>
    
        
    
  
        
        
        <div v-for="show in showDetails">
            <div class="">
                <div class="border border-top-5 m-2 p-3">
                    <div class="text-align-custom d-flex justify-content-around">
                        <div class="w-25 show-details-box">
                            <h4 class="card-title">{{ show[2] }}</h4>
                            <h5 class="card-subtitle mb-2">({{ show[6] }})</h5>
                            <h6 class="card-subtitle mb-2 text-muted">Number of Tickets: {{ show[4] }}</h6>
                            <h6 class="card-subtitle mb-2 text-muted">Total Cost: {{ show[5] }}</h6>
                        </div>
                        <div>
                            <button class="btn-red mt-5 mx-3" @click="deleteBooking(show[2], show[1], show[4])">Delete</button>
                        </div>
                    </div>
                </div>
            </div>
        </div>
        <div class="col-auto">
        <!-- Button on the left-most position -->
        <button class="btn btn-primary" @click="backToUserDashboard()">Back to User Dashboard</button>
      </div>
    </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

.seeTickets {
    font-family: 'Poppins', sans-serif;
    margin: 0;
}

.show-details-box{
    border: 1px solid #f55a5a;
    border-radius: 5px;
    padding: 10px;
    margin: 10px;
    background-color: #f2f2f2;
    height: 150%;
    width: 100%;
    text-align: center;
}

.btn-red {

    
    font-family: 'Poppins', sans-serif;
    background-color: #f55a5a; /* Green */
  border: none;
  color: white;
  padding: 15px 32px;
  text-align: center;
  text-decoration: none;
  display: inline-block;
  font-size: 16px;
  border-radius: 5px;

}
</style>


<script>
import axios from 'axios';

export default {
    name: 'seeTickets',
    data: function () {
        return {
            showDetails: [],
            username: this.$route.params.username,
        }
    },
    methods: {
        deleteBooking(showname, username, numberOfTickets){
            axios.post('http://127.0.0.1:5000/api/deleteUserBooking',
            {
                showname: showname,
                username: username,
                numberOfTickets: numberOfTickets
            }).then(response => {
                console.log(response.data);
                this.$router.go();
            }).catch(error => {
                console.log(error);
            })
        },
        backToUserDashboard(){
            this.$router.push({name: 'home',params: { username: this.username }});
        }

    },
    created() {
        axios.post('http://127.0.0.1:5000/api/getUserBookingDetails', {
            username: this.username
        }).then(response => {
            console.log(response.data);
            this.showDetails = response.data.userBookingDetails;
        }).catch(error => {
            console.log(error);
        })

    }
}
</script>