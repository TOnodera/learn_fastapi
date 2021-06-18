<template>
  <!-- App.vue -->

  <v-app>
    <side-bar />

    <v-app-bar app>
      <v-icon>fas fa-arrow-right</v-icon>
    </v-app-bar>
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
export default {
  name: 'Admin',
  components: {
    SideBar,
  },
};
</script>
