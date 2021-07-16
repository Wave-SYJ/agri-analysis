<template>
  <el-menu :default-active="currentRoutePath" router style="height: 100%">
    <fragment v-for="route in routes" :key="route.path">
      <el-menu-item v-if="!route.meta.hasChildren" :index="route.path">
        <i :class="route.meta.icon"></i>
        <span slot="title">{{ route.meta.title }}</span>
      </el-menu-item>
      <el-submenu v-else :index="route.path">
        <template slot="title">
          <i :class="route.meta.icon"></i>
          <span>{{ route.meta.title }}</span>
        </template>
        <el-menu-item v-for="subRoute in route.children" :key="subRoute.path" :index="subRoute.path">
          <i :class="subRoute.meta.icon"></i>
          <span slot="title">{{ subRoute.meta.title }}</span>
        </el-menu-item>
      </el-submenu>
    </fragment>
  </el-menu>
</template>

<script>
import { dashboardRoutes } from "@/routes";
export default {
  data() {
    return {
      routes: dashboardRoutes,
    };
  },
  computed: {
    currentRoutePath() {
      return this.$route.path
    }
  }
};
</script>

<style scoped>
</style>
