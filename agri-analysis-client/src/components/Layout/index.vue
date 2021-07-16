<template>
  <el-container style="height: 500px; border: 1px solid #eee">
    <el-header><Header /></el-header>
    <el-container>
      <el-aside width="300px"><MenuBar /></el-aside>
      <el-container>
        <el-main><router-view /></el-main>
      </el-container>
    </el-container>
    <el-footer><Footer /></el-footer>
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

<style>

</style>
