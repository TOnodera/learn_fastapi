<template>
  <!-- App.vue -->

  <v-app>
    <admin-nav />
    <side-bar />
    <v-main>
      <v-container fluid>
        <router-view></router-view>
      </v-container>
    </v-main>

    <v-footer app>
      <!-- -->
    </v-footer>
  </v-app>
</template>

<script>
import SideBar from './components/admin/SideBar';
import AdminNav from './components/admin/AdminNav';
export default {
  name: 'Admin',
  components: {
    SideBar,
    AdminNav,
  },
};
</script>
