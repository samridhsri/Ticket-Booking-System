<template>
    <div class="bg-custom">
        
        <div class="bg-light container h-75 p-5 vertical-custom rounded-5">
        <h1 class="display-4">Register/Login</h1>
        <div class="input-div">
            <p class="label-text">Enter your email-id here</p>
            <input class="input input-text-custom input-box rounded-5 text-center" placeholder="name@example.com" v-model="email" type="email">
        </div>
        <div class="input-div">
            <p class="label-text">Enter your password here</p>
            <input class="input input-text-custom input-box rounded-5 text-center" placeholder="password" v-model="password" type="password">
        </div>
        <div class="mt-4">
        <button class="button btn-danger btn-lg btn mx-5" @click="register()">Register</button>
        <button class="button btn btn-lg btn-danger mx-5" @click="login()">Login</button>
        </div>

    </div>
    </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
.bg-custom {
  background-image: url('https://i.imgur.com/NQQTWH9.png');
  height: 100vh;
}
.display-4{
    font-family: 'Poppins', sans-serif;
    font-size: 4rem;
    font-weight: 600 !important;
    line-height: 1.2;
    color: rgba(50, 6, 90, 1);
    margin-bottom: 1rem;
    margin-top: 1rem;
    text-align: center;
    letter-spacing: -3px;
}

.vertical-custom {
    top: 10%;
    width: 40rem !important;
}


.btn-danger, .btn-danger:hover, .btn-danger:active, .btn-danger:visited {
    background: linear-gradient(135deg, rgba(2,0,36,1) 0%, rgba(201,98,204,1) 0%, rgba(81,80,142,1) 100%);
    border: none !important;
}
.label-text{
    font-family: 'Poppins', sans-serif;
    font-size: 2rem;
    font-weight: 400 !important;
}

.input-div{
    margin: 1rem;

}

.input-box{
    width: 22rem;
    border-color: rgba(50, 6, 90, 1);
}
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
        register() {
            console.log(this.email);
            console.log(this.password);
            axios.post('http://127.0.0.1:5000/api/auth/register', {
                email: this.email,
                password: this.password
            }).then(response => {
                console.log(response.data);
            }).catch(error => {
                console.log(error);
            })
        },
        login() {
            axios.post('http://127.0.0.1:5000/api/auth/login', {
                email: this.email,
                password: this.password
            }).then(response => {
                console.log(response.data);
                const message = response.data.message;
                if (message === 'success') {
                    const token = response.data.access_token;
                    // const headers = { Authorization: `Bearer ${token}` };
                    localStorage.setItem('token', token);
                    localStorage.setItem('email', this.email);
                    this.$router.push('/home/');
                }
                else{
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