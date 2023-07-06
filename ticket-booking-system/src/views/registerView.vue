<template>
    <div>
        <h1>Register</h1>
        <p>
            <label>Email</label>
            <input class="input" placeholder="email" v-model="email" type="text">
        </p>
        <p>
            <label>password</label>
            <input class="input" placeholder="password" v-model="password" type="password">
        </p>
        <button class="button btn-primary btn is-primary" @click="register()">Register</button>

        {{ email }}
        {{ password }}


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
        register() {
            console.log(this.email);
            console.log(this.password);
            axios.post('http://127.0.0.1:5000/test', {
                email: this.email,
                password: this.password
            }).then(response => {
                console.log(response.data);
            }).catch(error => {
                console.log(error);
            })
        }
    }
}
</script>