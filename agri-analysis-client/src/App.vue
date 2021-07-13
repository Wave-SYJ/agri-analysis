<template>
  <div id="app">
    Hello
    <div><router-link to="/a">Go to A</router-link></div>
    <div><router-link to="/b">Go to B</router-link></div>

    <router-view></router-view>
  </div>
</template>

<script>
export default {
  name: 'App',
}
</script>

<style>
</style>
