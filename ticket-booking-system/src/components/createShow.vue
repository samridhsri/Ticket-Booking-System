<template>
    <div class="container">
        <div class="container">
            <div class="form-group">
                <input type="text" class="form-control" id="showName" v-model="name" placeholder="Enter Show Name">
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

            <button class="btn btn-primary mt-3" @click="createShow()">Save</button>

            
        </div>
    </div>
</template>

<script>
import axios from 'axios';

export default {
    name: 'CreateShow',
    data() {
        return {
            name: '',
            rating: '',
            time: '',
            tags: '',
            price: '',
            venuename: this.$route.params.venuename
        }

    },
    methods: {
        createShow() {
            console.log(this.name);
            console.log(this.rating);
            console.log(this.time);
            console.log(this.tags);
            console.log(this.price);
            console.log(this.venuename);
            axios.post('http://127.0.0.1:5000/api/createshow', {
                name: this.name,
                rating: parseInt(this.rating),
                time: this.time,
                tags: this.tags,
                price: parseInt(this.price),
                venuename: this.venuename
            }).then(response=> {
                console.log(response.data);
            }).catch(error => {
                console.log(error);
            })

    },
    created() {
        
    }
}
}

</script>