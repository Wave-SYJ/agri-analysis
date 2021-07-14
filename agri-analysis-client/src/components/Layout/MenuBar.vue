<template>
<el-aside>
  <ul class="menu-bar">
    <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    <el-menu :default-openeds="['1', '4']">
      <el-menu-item index="1">
        <template slot="title"><i class="el-icon-view"></i><router-link to="/a" class="a">数据监控</router-link></template>
      </el-menu-item>
      <el-submenu index="2">
        <template slot="title"><i class="el-icon-search"></i><router-link to="/b" class="a">数据查询</router-link></template>
        <el-menu-item index="2-1" style="color=rgb(0,0,0)"><i class="el-icon-location-outline"></i>区域行情</el-menu-item>
        <el-menu-item index="2-1" style="color=rgb(0,0,0)"><i class="el-icon-ship"></i>品种对比</el-menu-item>
        <el-menu-item index="2-1" style="color=rgb(0,0,0)"><i class="el-icon-cherry"></i>农产品售卖行情</el-menu-item>
      </el-submenu>
      <el-menu-item index="3">
        <template slot="title"><i class="el-icon-data-line" ></i>数据预测</template>
      </el-menu-item>
      <el-submenu index="4">
        <template slot="title"><i class="el-icon-edit"></i>数据修改</template>
      </el-submenu>
    </el-menu>
  </el-aside>
  
  </ul>
</el-aside>
</template>

<script>
export default {};
</script>

<style scoped>
.menu-bar {
  padding-top: 10px;
  height: 620px;
  width: 100px;
  background-color: rgb(255, 255, 255);
  color: #333;
}
.a{
  text-decoration: none;
  color: black;
}

</style>
