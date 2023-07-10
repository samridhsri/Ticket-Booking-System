<template>
    <div>
        <button class="btn btn-primary text-center my-auto" v-if="venueListIsEmpty()" @click="createVenue()">+</button>

        <div class="container">
            <h1>Hello Admin</h1>
            <div class="container border p-5" v-for="venue in venues">
                <h1 class="">{{ venue[1] }}</h1>
                <div class="row col-lg-12 px-5 mx-auto mb-4">
                    <div class="card" style="width: 18rem;" v-for="show in venueAndShows[venue[1]]">
                        <div class="card-body">
                            <div class="">
                                <h5 class="card-title">{{ show[1] }}</h5>
                                <h6 class="card-subtitle mb-2 text-body-secondary">time: {{ show[3] }}</h6>
                            </div>

                            <button type="button" class="btn btn-primary mt-3 mx-2" @click="editShow(show[1])">Edit</button>
                            <button type="button" class="btn btn-primary mt-3 mx-2" @click="deleteShow(show[1])">Delete</button>
                        </div>
                    </div>
                </div>
                <button @click="createShow(venue[1])">Add Shows</button>
            </div>
            <button class="btn btn-primary text-center my-auto mt-5" v-if="!venueListIsEmpty()" @click="createVenue()">+</button>
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            //Data variables
            venues: [],
            shows: [],
            venueAndShows: {}
        }
    },
    methods: {
        //Methods
        editShow(showname) {
            this.$router.push({ name: 'editShow', params: { showname: showname } })
        },

        deleteShow(showname) {
            axios.post('http://127.0.0.1:5000/api/deleteShow', {
                showname: showname
            }).then(response => {
                console.log(response.data);
                this.$router.go()
            }).catch(error => {
                console.log(error);
            })
        },

        createVenue() {
            this.$router.push({ name: 'createVenue' })
        },
        venueListIsEmpty() {
            return this.venues.length == 0;
        },
        createShow(venueName) {
            this.$router.push({ name: 'createShow', params: { venuename: venueName } })
        }
    },
    created() {
        //On page load check if there are venues in the database
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
    }
}
</script>