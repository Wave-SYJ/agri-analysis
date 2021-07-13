<template>
  <el-container>
    <el-header><Header /></el-header>
    <el-container>
      <el-aside width="200px"><MenuBar /></el-aside>
      <el-container>
        <el-main><router-view /></el-main>
        <el-footer><Footer /></el-footer>
      </el-container>
    </el-container>
  </el-container>
</template>

<script>
import Header from './Header.vue';
import MenuBar from './MenuBar.vue';
import Footer from './Footer.vue';

export default {
  components: {
    Header,
    MenuBar,
    Footer
  }
};
</script>

<style></style>
