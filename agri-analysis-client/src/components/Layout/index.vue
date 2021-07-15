<template>
  <countainer>
    <el-header style="padding: 0"><Header /></el-header>
    <el-container>
      <el-aside width="200px"><MenuBar /></el-aside>
      <el-container>
        <el-main><router-view /></el-main>
      </el-container>
    </el-container>
    <el-footer style="border-top: solid 1px #e6e6e6;"><Footer /></el-footer>
  </countainer>
</template>

<script>
import Header from "./Header.vue";
import MenuBar from "./MenuBar.vue";
import Footer from "./Footer.vue";

export default {
  components: {
    Header,
    MenuBar,
    Footer,
  },
};
</script>

<style>
</style>
