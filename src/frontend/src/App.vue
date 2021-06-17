<template>
  <v-app>
    <v-app-bar app color="primary" dark>
      <header>
        <v-app-bar app color="primary" dark>
          <v-toolbar-title>Fast Posting</v-toolbar-title>
        </v-app-bar>
      </header>
    </v-app-bar>

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
