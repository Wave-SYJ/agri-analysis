<template>
  <div class="header-container">
    <a class="header-icon-wrapper" href="/">
      <el-image
        class="header-icon"
        fit="contain"
        :src="require('@/assets/images/logo.png')"
      ></el-image>
    </a>
    <div class="header-title">农产品数据分析系统</div>
    <div class="header-user">
      <el-link :underline="false" type="primary" @click="$router.push('/login')">登录</el-link>
    </div>
  </div>
</template>

<script>
export default {};
</script>

<style scoped lang="scss">
.header-container {
  height: 100%;
  width: 100%;
  background-color: #ebf1f6;
  display: flex;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
  position: relative;
  z-index: 10;

  .header-icon-wrapper {
    display: block;
    width: 200px;
    text-align: center;
    flex: none;

    .header-icon {
      width: 120px;
    }
  }

  .header-title {
    flex: auto;
    text-align: center;
    font-size: 20px;
    line-height: 60px;
    font-weight: bold;
  }

  .header-user {
    flex: none;
    line-height: 60px;
    margin-right: 30px;
  }
}
</style>