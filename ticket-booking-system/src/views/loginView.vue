
<template>
    <div>
        <h1>Login</h1>
        <p>
            <label>Email</label>
            <input class="input" v-model="email" type="email">
        </p>
        <p>
            <label>password</label>
            <input v-model="password" type="password">
        </p>
        <button class="button btn-primary btn is-primary" @click="login()">Login</button>


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

<style></style>

