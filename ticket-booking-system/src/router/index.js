import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import loginView from '../views/loginView.vue'
import registerView from '../views/registerView.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'home',
    component: HomeView
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: function () {
      return import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
    }
  },{
    path: '/login',
    name: 'login',
    component: loginView
  },
  {
    path: '/register',
    name: 'register',
    component: registerView
  }
]

const router = new VueRouter({
  routes
})

export default router
