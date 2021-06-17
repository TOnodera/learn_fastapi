<template>
  <v-app>
    <v-app-bar app color="primary" dark> </v-app-bar>

    <v-main>
      <layout />
    </v-main>
  </v-app>
</template>

<script>
import Layout from './components/admin/Layout';

export default {
  name: 'App',

  components: {
    Layout,
  },

  data: () => ({
    //
  }),
};
</script>
