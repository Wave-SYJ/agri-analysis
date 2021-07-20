<template>
  <div style="display: flex">
    <el-input
      style="flex: auto"
      v-model="value[0]"
      @input="$emit('input', [value[0], $event.target.value])"
    />
    <span style="flex: none; margin: 0 10px">-</span>
    <el-input
      style="flex: auto"
      v-model="value[1]"
      @input="$emit('input', [$event.target.value], value[1])"
    />
  </div>
</template>

<script>
export default {
  props: {
    value: Array,
  },
};
</script>

<style>
</style>