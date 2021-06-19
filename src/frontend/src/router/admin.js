import Vue from 'vue';
import VueRouter from 'vue-router';
import Admin from '../views/admin/Admin';
import User from '../views/admin/user/User';
import UserCreate from '../views/admin/user/Create';

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
  {
    path: '/admin/user/create',
    name: 'UserCreate',
    component: UserCreate,
  },
];

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes,
});

export default router;
