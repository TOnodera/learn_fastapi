<template>
  <v-app>
    <admin-nav @hamberger-click="hambergerClicked" />
    <side-bar :hamberger-toggle="hambergerToggle" />
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
  data() {
    return {
      hambergerToggle: false,
    };
  },
  methods: {
    hambergerClicked: function () {
      this.hambergerToggle = !this.hambergerToggle;
    },
  },
};
</script>
