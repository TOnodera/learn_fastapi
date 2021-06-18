<template>
  <v-app-bar class="nav" app>
    <div class="icon-wrapper">
      <p class="icon"><v-icon>fas fa-arrow-right</v-icon></p>
      <p class="text">サイトを見る</p>
    </div>
  </v-app-bar>
</template>

<style lang="scss" scoped>
.nav {
  display: flex;
  justify-content: flex-end;
  .icon-wrapper {
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
