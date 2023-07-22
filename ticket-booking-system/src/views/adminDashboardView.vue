<template>
    <div>
        <button class="btn btn-primary text-center my-auto" v-if="venueListIsEmpty()" @click="createVenue()">+</button>

        <div class="container">
            <h1>Hello Admin</h1>
            <div class="container border border-bottom-5 venue-container " v-for="venue in venues">
                <div class="">
                    <h1 class="">{{ venue[1] }}</h1>
                </div>
                <div class="row col-lg-12 px-5 mx-auto mb-4">
                    <div class="card" style="width: 18rem;" v-for="show in venueAndShows[venue[1]]">
                        <div class="card-body">
                            <div class="">
                                <h5 class="card-title">{{ show[1] }}</h5>
                                <h6 class="card-subtitle mb-2 text-body-secondary">time: {{ show[3] }}</h6>
                            </div>

                            <button type="button" class="btn btn-primary mt-3 mx-2" @click="editShow(show[1])">Edit</button>
                            <button type="button" class="btn btn-primary mt-3 mx-2"
                                @click="deleteShow(show[1],show[3])">Delete</button>
                        </div>
                    </div>
                </div>
                <button class="btn btn-primary" @click="createShow(venue[1], venue[4])">Add Shows</button>
            </div>
            <button class="btn btn-primary text-center my-auto mt-5 mx-4" v-if="!venueListIsEmpty()"
                @click="createVenue()">+</button>
            <button class="btn btn-primary text-center my-auto mt-5" @click="exportVenuePDF()">Export Venue Details</button>
            <button class="btn btn-primary text-center my-auto mx-3 mt-5" @click="exportShowDetails()">Export Show Details</button>
            
        </div>
    </div>
</template>

<style>
.venue-container {
    border-radius: 10px;
    padding: 10px;
    margin: 10px;
    background-color: #f2f2f2;
    height: 150%;
}
</style>

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

        deleteShow(showname, showtime) {
            axios.post('http://127.0.0.1:5000/api/deleteShow', {
                showname: showname,
                time: showtime
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
        createShow(venueName, venuecapacity) {
            this.$router.push({
                name: 'createShow', params: {
                    venuename: venueName,
                    venuecapacity: venuecapacity
                }
            })
        },
        async exportVenuePDF() {
    const data = [
        (this.venues, this.shows, this.venueAndShows)
    ];

    try {
        const response = await axios.post('http://127.0.0.1:5000/api/exportVenuePDF', data);
        const pdf_file = response.data.pdf_file;

        // Check if the browser supports the "FileSaver" API for saving files
        if (window.navigator.msSaveOrOpenBlob) {
            // For IE/Edge (use the "downloadPDF" endpoint to download the file)
            window.location.href = `http://127.0.0.1:5000/api/downloadVenuePDF/${pdf_file}`;
        } else {
            // For other browsers (use a link to download the file)
            const downloadLink = document.createElement('a');
            downloadLink.href = `http://127.0.0.1:5000/api/downloadVenuePDF/${pdf_file}`;
            downloadLink.target = '_blank';
            downloadLink.download = 'venue_details.pdf';
            downloadLink.click();
        }

        alert('PDF Generated');
    } catch (error) {
        console.error(error);
        alert('Failed to generate PDF. Please try again.');
    }
},
async exportShowDetails(){
    const data = [(this.show)]

    try {
        const response = await axios.post('http://127.0.0.1:5000/api/exportShowPDF', data);
        const pdf_file = response.data.pdf_file;

        if(window.navigator.msSaveOrOpenBlob){
            window.location.href = `http://127.0.0.1:5000/api/downloadShowPDF/${pdf_file}`;
        }else{
            const downloadLink = document.createElement('a');
            downloadLink.href = `http://127.0.0.1:5000/api/downloadShowPDF/${pdf_file}`;
            downloadLink.target = '_blank';
            downloadLink.download = 'show_details.pdf';
            downloadLink.click();
        }
        alert('PDF Generated');
    } catch (error) {
        console.error(error);
        alert('Failed to generate PDF. Please try again.');
    }

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