<template>
    <div class="container">
            <div class="form-group">
                <label for="venueName">Venue Name</label>
                <input type="text" class="form-control" id="venueName" v-model="name" placeholder="Enter Venue Name">

            </div>
            <div class="form-group">
                <label for="venuePlace">Place</label>
                <input type="text" class="form-control" id="venuePlace" v-model="place"
                    placeholder="Enter Place: Example IITM">
            </div>
            <div class="form-group">
                <label for="venueLocation">Location</label>
                <input type="text" class="form-control" id="venueLocation" v-model="location"
                    placeholder="Enter Location: Example Chennai">
            </div>
            <div class="form-group">
                <label for="venueCapacity">Capacity</label>
                <input type="text" class="form-control" id="venueCapacity" v-model="capacity"
                    placeholder="Enter Capacity: Example 250">
            </div>
            <button class="btn btn-primary mt-3" @click="createVenue()">Submit</button>

    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'CreateVenue',
    data() {
        return {
            name: '',
            place: '',
            location: '',
            capacity: ''
        }
    },
    methods: {
        createVenue() {
            axios.post('http://127.0.0.1:5000/api/createVenue',
            {
                name: this.name,
                place: this.place,
                location: this.location,
                capacity: this.capacity
            }
            ).then(
                response => {
                    console.log(response.data);
                    this.$router.push({ name: 'adminDashboard' })
                }
            ).catch(error => {
                console.log(error);
            }
            );
        }

    }
}
</script>