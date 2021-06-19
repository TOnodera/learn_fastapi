<template>
  <v-breadcrumbs :items="items">
    <template v-slot:divider>
      <v-icon>mdi-chevron-right</v-icon>
    </template>
  </v-breadcrumbs>
</template>

<script>
export default {
  name: 'Breadcrumbs',
  data() {
    return {
      items: [],
    };
  },
  mounted() {
    const paths = this.$route.path.split('/').filter((value) => value);
    let href = '';
    paths.forEach((value, index) => {
      href += `/${value}`;
      this.items.push({
        text: value,
        disabled: index === paths.length - 1,
        href: href,
      });
    });
  },
};
</script>
