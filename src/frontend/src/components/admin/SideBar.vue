<template>
  <v-navigation-drawer app>
    <v-list-item>
      <v-list-item-content>
        <v-list-item-title class="text-h6"> FastApi Admin </v-list-item-title>
        <v-list-item-subtitle> 管理画面 </v-list-item-subtitle>
      </v-list-item-content>
    </v-list-item>
    <v-divider></v-divider>
    <v-list dense nav>
      <v-list-item v-for="item in items" :key="item.title" link>
        <v-list-item-icon>
          <v-icon>{{ item.icon }}</v-icon>
        </v-list-item-icon>

        <v-list-item-content>
          <router-link :to="item.to">
            <v-list-item-title>{{ item.title }}</v-list-item-title>
          </router-link>
        </v-list-item-content>
      </v-list-item>
    </v-list>
  </v-navigation-drawer>
</template>

<script>
export default {
  data() {
    return {
      items: [
        { title: 'Dashboard', icon: 'mdi-view-dashboard', to: '/admin' },
        { title: 'User', icon: 'fas fa-male', to: '/admin/user' },
      ],
      right: null,
    };
  },
};
</script>
