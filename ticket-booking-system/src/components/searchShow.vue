<template>
    <div class="home ">
        
        <div class="d-flex flex-wrap justify-content-around mt-4">
            <div>
                <h3 class="text-sm-left">Please Be Patient</h3>
                <h5>Looking for {{ showName }}</h5>

            </div>
            <div>
                <input type="text" class="form-control" placeholder="Search for a show" aria-label="Search for a show"
                    @keyup.enter="searchShow(searchForShow)" v-model="searchForShow" aria-describedby="button-addon2">
            </div>

            

        </div>
        <div>
                
        </div>
        <div class="d-flex flex-wrap">
            <div class="container bg-active d-flex w-25 mx-3 h-100" v-for="show in showDetails">
                <div class="bg-custom-card">
                    <div class="text-center"><h3>{{ show[1] }}</h3></div>
                    <div class="text-center"><h5>Timing: {{ show[3] }}</h5></div>
                    <div class="text-center"><h5>Genre: {{ show[4] }}</h5></div>
                    <div class="text-center"><h5>Number of Tickets: {{ show[2] }}</h5></div>
                    <div class="text-center"><h5>Price: {{ show[5] }}</h5></div>
                    <div class="text-center"><h5>Rating: {{ show[2] }}</h5></div>
                    <div class="text-center"><h5>Venue: {{ show[6] }}</h5></div>
                </div>
            </div>
        </div>
        <div class="">
            <button class="btn btn-primary" @click="goToHome()">Go back to Home</button>
        </div>
        
    </div>
</template>

<style scoped>
.bg-custom-card{
    background-color: #e6e6e6;
    border-radius: 10px;
    padding: 10px;
    margin: 10px;
    width: 20em;
    height: 14em;
    box-shadow: 0 0 10px rgba(0,0,0,0.5);
    padding-top: 1.5em;
}
</style>

<script>
import axios from 'axios';

export default {
    name: 'searchShow',
    data: function () {
        return {
            showName: this.$route.params.showName,
            showDetails: {},
            searchForShow: ''
        }
    },
    methods: {
        searchShow(showName) {
            console.log(showName);
            this.$router.push({ name: 'searchShow', params: { showName: showName } });
            this.$router.go();
        },
        goToHome() {
            this.$router.push({ name: 'home' });
            this.$router.go();
        }
    },
    created() {
        console.log(this.showName);
        axios.post('http://127.0.0.1:5000/api/show-search',
            { showName: this.showName })
            .then(response => {
                console.log(response.data);
                this.showDetails = response.data.showDetails;
            })
            .catch(error => {
                console.log(error);
            });
    }
}

</script>