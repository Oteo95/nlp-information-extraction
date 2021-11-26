import Vue from 'vue'
import VueRouter from 'vue-router'

Vue.use(VueRouter)

const routes = [
  {
    path: '/tagger',
    name: 'Tagger',
    component: () => import('../views/Tagger.vue'),
    meta: {
      requiresAuth: true
    }
  },
  {
    path: '/',
    name: 'Documents',
    component: () => import('../views/DocTables.vue'),
    meta: {
      requiresAuth: true
    }
  },

]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: routes
})

export default router
