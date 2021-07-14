<template>
  <el-menu
    default-active="2"
    class="el-menu-vertical-demo"
    @open="handleOpen"
    @close="handleClose"
  >
    <el-menu-item index="1">
      <i class="el-icon-menu"></i>
      <span slot="title">数据更新</span>
    </el-menu-item>
    <el-submenu index="2">
      <template slot="title">
        <i class="el-icon-location"></i>
        <span>数据查询</span>
      </template>
      <el-menu-item index="2-1">区域行情查询</el-menu-item>
      <el-menu-item index="2-2">品种对比</el-menu-item>
      <el-menu-item index="2-3">售卖行情</el-menu-item>
    </el-submenu>

    <el-menu-item index="3">
      <i class="el-icon-document"></i>
      <span slot="title">数据预测</span>
    </el-menu-item>

    <el-menu-item index="4">
      <i class="el-icon-setting"></i>
      <span slot="title">数据修改</span>
    </el-menu-item>
  </el-menu>
</template>

<script>
export default {
  methods: {
    handleOpen(key, keyPath) {
      console.log(key, keyPath);
    },
    handleClose(key, keyPath) {
      console.log(key, keyPath);
    },
  },
};
</script>
