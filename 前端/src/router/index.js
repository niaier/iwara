import Vue from 'vue'
import VueRouter from 'vue-router'
import Home from '../views/Home.vue'
import Video from '../views/Video.vue'
import Play from '../views/Play.vue'
import Love from '../views/Love.vue'
import PlayList from '../views/PlayList.vue'

Vue.use(VueRouter)
const originalPush = VueRouter.prototype.push
VueRouter.prototype.push = function push(location) {
  return originalPush.call(this, location).catch(err => err)
}
const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/video',
    name: 'Video',
    component: Video
  },
  {
    path: '/play/:videoId',
    name: 'Play',
    component: Play
  },
  {
    path: '/love',
    name: 'Love',
    component: Love
  },
  {
    path: '/playlist',
    name: 'PlayList',
    component: PlayList
  },
  {
    path: '/about',
    name: 'About',
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () => import(/* webpackChunkName: "about" */ '../views/About.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
