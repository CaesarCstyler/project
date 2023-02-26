import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/HomeView.vue'

import Sneakers from '../views/SneakersView.vue'
import Category from '../views/CategoryView.vue'
import Search from '../views/SearchView.vue'
import Cart from '../views/CartView.vue'
import SignUp from '../views/SignUpView.vue'
import LogIn from '../views/LogInView.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/about',
    name: 'about',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/AboutView.vue')
  },
  {
    path: '/sign-up',
    name: 'SignUp',
    component: SignUp
  },
  {
    path: '/log-in',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/search',
    name: 'Search',
    component: Search
  },
  {
    path: '/cart',
    name: 'Cart',
    component: Cart
  },
  {
    path: '/:category_slug/:sneakers_slug',
    name: 'Sneakers',
    component: Sneakers
  },
  {
    path: '/:category_slug',
    name: 'Category',
    component: Category
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
