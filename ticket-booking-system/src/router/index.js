import Vue from 'vue'
import VueRouter from 'vue-router'
import HomeView from '../views/HomeView.vue'
import adminloginView from '../views/adminloginView.vue'
import loginView from '../views/loginView.vue'
import introView from '../views/introView.vue'
import adminDashboardView from '../views/adminDashboardView.vue'
import createVenue from '../components/createVenue.vue'
import createShow from '../components/createShow.vue'
import editShow from '../components/editShow.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'intro',
    component: introView
  },
  {
    path: '/home',
    name: 'home',
    component: HomeView,
    meta: {
      // requiresAuth: true
    }
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
    path: '/admin-login',
    name: 'admin-login',
    component: adminloginView
  },
  {
    path: '/login',
    name: 'login',
    component: loginView
  },
  {
    path: '/adminDashboard',
    name: 'adminDashboard',
    component: adminDashboardView
  },
  {
    path: '/createVenue',
    name: 'createVenue',
    component: createVenue
  },
  {
    path: '/createShow/:venuename',
    name: 'createShow',
    component: createShow
  },
  {
    path: '/editShow/:showname',
    name: 'editShow',
    component: editShow
  }
]

const router = new VueRouter({
  routes
})

router.beforeEach((to, from, next) => {
  const isAuthenticated = !!localStorage.getItem('token'); // Check if token exists
  if (to.meta.requiresAuth && !isAuthenticated) {
    // Redirect to the login page or another unauthorized page
    next('/login');
  } else {
    next();
  }
});


export default router
