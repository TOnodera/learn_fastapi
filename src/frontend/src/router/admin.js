import Vue from 'vue';
import VueRouter from 'vue-router';
import Admin from '../views/admin/Admin';
import User from '../views/admin/user/User';

Vue.use(VueRouter);

const routes = [
  {
    path: '/admin',
    name: 'Admin',
    component: Admin,
  },
  {
    path: '/admin/user',
    name: 'User',
    component: User,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
