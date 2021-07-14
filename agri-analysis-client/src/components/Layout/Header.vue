<template>
  <!--<div class="header">农产品数据分析系统</div>-->
  <el-header>
      <!--<div style="text-align: center; font-size: 30px" >农产品数据分析系统</div>-->
      <el-dropdown style="text-align: right; font-size: 30px;">
        <i class="el-icon-setting" style="margin-right: 20px"></i>
        <el-dropdown-menu slot="dropdown">
        <!--<el-dropdown-item>切换主题</el-dropdown-item>
          <el-dropdown-item>切换语言</el-dropdown-item>-->
          <el-dropdown-item>网页简介</el-dropdown-item>
        </el-dropdown-menu>
      </el-dropdown>
    </el-header>
</template>

<script>
export default {

}
</script>

<style scoped>

.el-header {
  width: 100%;
  height: 40px;
  background-color: rgb(255, 255, 255);
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}

</style>