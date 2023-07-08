
<template>
    <div>
        <h1>Admin Login</h1>
        <p>
            <label>Email</label>
            <input class="input" v-model="email" type="email">
        </p>
        <p>
            <label>password</label>
            <input v-model="password" type="password">
        </p>
        <button class="button btn-primary btn is-primary" @click="adminlogin()">Login</button>


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

