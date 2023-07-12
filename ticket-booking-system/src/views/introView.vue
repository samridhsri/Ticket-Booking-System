<template>
  <div class="home bg-custom">
    <!-- <Navbar /> -->
    <div class="container">
      <div class="vertical-center">
      <h1 class="display-3">
        Explore, Book and Discover College Entertainment
      </h1>
    </div>
    </div>

  </div>
</template>

<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@800&display=swap');

.container {
  height: 200px;
  position: relative;
  border: 3px
}

.bg-custom {
  background-image: url('https://i.imgur.com/NQQTWH9.png');
  height: 100vh;
}


.vertical-center {
  margin: 0;
  margin-top: 30vh;
  position: absolute;
  top: 50%;
  -ms-transform: translateY(-50%);
  transform: translateY(-50%);
}

.display-3 {
  font-family: 'Poppins', sans-serif;
  font-size: 5rem;
  font-weight: 600 !important;
  line-height: 1.2;
  color: whitesmoke;
  margin-bottom: 1rem;
  margin-top: 1rem;
  text-align: center;
  letter-spacing: -3px;
}
</style>
<script>
import Navbar from '../components/Navbar.vue'


export default {
  name: 'introView',
  components: {
    Navbar,
  },
}
</script>
  