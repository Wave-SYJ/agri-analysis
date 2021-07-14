<template>
<el-aside>
  <ul class="menu-bar">
    <el-aside width="200px" style="background-color: rgb(238, 241, 246)">
    <el-menu>
      <el-menu-item index="1">
        <template slot="title"><i class="el-icon-view"></i><router-link to="/dashboard/a" class="a">数据监控</router-link></template>
      </el-menu-item>
      <el-submenu index="2">
        <template slot="title"><i class="el-icon-search"></i>数据查询</template>
        <el-menu-item index="2-1" style="color=rgb(0,0,0)"><i class="el-icon-location-outline"></i><router-link to="/dashboard/b/a" class="a">区域行情</router-link></el-menu-item>
        <el-menu-item index="2-1" style="color=rgb(0,0,0)"><i class="el-icon-ship"></i><router-link to="/dashboard/b/b" class="a">品种对比</router-link></el-menu-item>
        <el-menu-item index="2-1" style="color=rgb(0,0,0)"><i class="el-icon-cherry"></i><router-link to="/dashboard/b/c" class="a">售卖行情</router-link></el-menu-item>
      </el-submenu>
      <el-menu-item index="3">
        <template slot="title"><i class="el-icon-data-line" ></i><router-link to="/dashboard/c" class="a">数据预测</router-link></template>
      </el-menu-item>
      <el-submenu index="4">
        <template slot="title"><i class="el-icon-edit"></i>数据管理</template>
        <el-menu-item index="4-1" style="color=rgb(0,0,0)"><i class="el-icon-edit-outline"></i><router-link to="/dashboard/d/a" class="a">数据确认</router-link></el-menu-item>
        <el-menu-item index="4-2" style="color=rgb(0,0,0)"><i class="el-icon-user"></i><router-link to="/dashboard/d/b" class="a">用户管理</router-link></el-menu-item>
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
