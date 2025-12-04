import { createRouter, createWebHistory } from 'vue-router'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: () => import('../views/HomePage.vue')
  },
  {
    path: '/login',
    name: 'Login',
    component: () => import('../views/LoginPage.vue')
  },
  {
    path: '/user-center',
    name: 'UserCenter',
    component: () => import('../views/UserCenterPage.vue')
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router

