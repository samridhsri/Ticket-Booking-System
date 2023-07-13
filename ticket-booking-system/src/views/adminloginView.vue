
<template>
    <div class="bg-custom">

        <div class="bg-light container h-75 p-5 vertical-custom rounded-5">
            <h1 class="display-4">Admin Login</h1>
            <div class="input-div">
                <p class="label-text">Enter your email-id here</p>
                <input class="input input-text-custom input-box text-center rounded-5" placeholder="name@example.com"
                    v-model="email" type="text">
            </div>
            <div class="input-div">
                <p class="label-text">Enter your password here</p>
                <input class="input input-text-custom input-box rounded-5 text-center" placeholder="password"
                    v-model="password" type="password">
            </div>
            <div class="mt-4">
                <button class="button btn-danger btn-lg btn" @click="adminlogin()">Login</button>
            </div>

        </div>
    </div>
</template>


<script>
import axios from 'axios';

export default {
    data() {
        return {
            email: '',
            password: ''
        };
    },
    methods: {
        adminlogin() {
            axios.post('http://127.0.0.1:5000/api/auth/admin-login', {
                email: this.email,
                password: this.password
            }).then(response => {
                console.log(response.data);
                const message = response.data.message;
                if (message === 'success') {
                    const token = response.data.access_token;
                    // const headers = { Authorization: `Bearer ${token}` };
                    localStorage.setItem('token', token);
                    this.$router.push('/adminDashboard/');
                }
                else {
                    alert('Invalid Credentials');
                }
            }).catch(error => {
                console.log(error);
            }
            )
        }
    }
}

</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');

.label-text {
    font-family: 'Poppins', sans-serif;
    font-size: 1.5rem;
    font-weight: 400 !important;
    letter-spacing: -1px;
}

.input-text-custom {
    font-family: 'Poppins', sans-serif;
}
</style>

