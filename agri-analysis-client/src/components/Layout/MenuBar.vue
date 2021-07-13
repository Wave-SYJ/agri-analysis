<template>
  <ul class="menu-bar">
    <li><router-link to="/dashboard/a">Go to A</router-link></li>
    <li><router-link to="/dashboard/b">Go to B</router-link></li>
  </ul>
</template>

<script>
export default {};
</script>

<style scoped>
.menu-bar {
  padding-top: 10px;
  height: 200px;
  width: 100px;
  background-color: orange;
}
</style>
