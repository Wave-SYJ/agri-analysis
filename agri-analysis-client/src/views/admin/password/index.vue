<template>
  <div class="password-form-wrapper">
    <el-form class="password-form" status-icon label-width="100px">
      <el-form-item label="原密码" prop="oldPassword">
        <el-input
          type="password"
          v-model="passwordObj.oldPassword"
          autocomplete="off"
        />
      </el-form-item>
      <el-form-item label="新密码" prop="newPassword">
        <el-input
          type="password"
          v-model="passwordObj.newPassword"
          autocomplete="off"
        />
      </el-form-item>
      <el-form-item label="确认密码" prop="checkPassword">
        <el-input
          type="password"
          v-model="passwordObj.checkPassword"
          autocomplete="off"
        />
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="submitForm('ruleForm')">
          提交
        </el-button>
        <el-button @click="passwordObj = {}">清空</el-button>
      </el-form-item>
    </el-form>
  </div>
</template>

<script>
export default {
  data() {
    return {
      passwordObj: {},
    };
  },
};
</script>

<style scoped lang="scss">
.password-form-wrapper {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100%;
  width: 100%;

  .password-form {
    width: 40%;
    min-width: 600px;
  }
}
</style>