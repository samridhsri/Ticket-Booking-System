<template>
<div class="container">
    <h1>Edit Show</h1>
        <div class="container">
            <div class="">
                Edit Show: {{ name }}
            </div>
            <div class="form-group">
                <input type="text" class="form-control" id="showRating" v-model="rating" placeholder="Enter Rating">
            </div>
            <div>
                <input type="text" class="form-control" id="showTime" v-model="time" placeholder="Enter Timing">
            </div>
            <div>
                <input type="text" class="form-control" id="showTags" v-model="tags" placeholder="Enter Tags">
            </div>
            <div>
                <input type="text" class="form-control" id="showPrice" v-model="price" placeholder="Enter Price">
            </div>
            <div>
                <input type="text" class="form-control" id="showVenueName" v-model="venuename" :placeholder=venuename>
            </div>

            <button class="btn btn-primary mt-3" @click="editShow()">Save</button>

            
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    data() {
        return {
            name: '',
            rating: '',
            time: '',
            tags: '',
            price: '',
            venuename: '',
            showname: this.$route.params.showname
        }
    },
    methods: {
        editShow() {
            axios.post('http://127.0.0.1:5000/api/editShowDetails', {
                showname: this.showname,
                rating: this.rating,
                time: this.time,
                tags: this.tags,
                price: this.price,
                venuename: this.venuename
            }).then(response => {
                console.log(response.data);
                this.$router.push({ name: 'adminDashboard' })
            }).catch(error => {
                console.log(error);
            })
            }
    },
    created() {
        axios.post('http://127.0.0.1:5000/api/showDetails', {
            showname: this.showname
        }).then(response => {
            console.log(response.data.showDetails[0]);
            this.name = response.data.showDetails[0][1];
            this.rating = response.data.showDetails[0][2];
            this.time = response.data.showDetails[0][3];
            this.tags = response.data.showDetails[0][4];
            this.price = response.data.showDetails[0][5];
            this.venuename = response.data.showDetails[0][6];

            console.log(this.name);
            console.log(this.rating);
            console.log(this.time);
            console.log(this.tags);
            console.log(this.price);
            console.log(this.venuename);
            
        }).catch(error => {
            console.log(error);
        })
    }
}

</script>