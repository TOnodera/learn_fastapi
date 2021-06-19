<template>
  <v-app-bar class="nav" app>
    <v-app-bar-nav-icon @click="hambergerClickedEmitter"></v-app-bar-nav-icon>
    <div class="icon-wrapper">
      <p class="icon"><v-icon>fas fa-arrow-right</v-icon></p>
      <p class="text" @click="toTopPage">サイトを見る</p>
    </div>
  </v-app-bar>
</template>

<script>
export default {
  name: 'AdminNav',
  methods: {
    toTopPage() {
      window.open('/', '_blank');
    },
    hambergerClickedEmitter() {
      this.$emit('hamberger-click');
    },
  },
};
</script>

<style lang="scss" scoped>
.nav {
  display: flex;
  justify-content: flex-end;
  .icon-wrapper {
    &:hover {
      cursor: pointer;
    }
    margin-top: 10px;
    display: flex;
    flex-flow: wrap;
    justify-content: space-around;
    width: 70px;
    .icon {
      margin-bottom: 0;
    }
    .text {
      font-size: 10px;
    }
  }
}
</style>
