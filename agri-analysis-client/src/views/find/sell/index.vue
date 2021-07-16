<template>
  <div class="page-wrapper">
    <el-form inline label-position="right" class="search-pane">
      <el-form-item label="地区">
        <el-cascader
          collapse-tags
          :options="regionList"
          v-model="searchMarket"
          :props="{ multiple: true }"
          clearable
        />
      </el-form-item>

      <el-form-item label="种类">
        <el-cascader
          collapse-tags
          :options="regionList"
          v-model="searchType"
          :props="{ multiple: true }"
          clearable
        />
      </el-form-item>

      <el-form-item>
        <el-button type="primary" @click="queryclick">查询</el-button>
      </el-form-item>
    </el-form>

    <div style="margin-bottom: 20px">您查询的农作物数据天数为：{{ dayCount }}</div>
    <div>
      选择显示的时间间隔：
      <el-select placeholder="请选择">
        <el-option label="年" value="year" />
        <el-option label="月" value="month" />
        <el-option label="日" value="day" />
      </el-select>
      <el-button style="margin-left: 20px">确认</el-button>
    </div>
  </div>
</template>

<script>
import regionList from "./fakeRegionData";
export default {
  data() {
    return {
      regionList,
      searchMarket: null,
      searchType: null,
      dayCount: 0,
    };
  },
  methods: {
    queryclick() {
      console.log(this.searchMarket, this.searchType);
      this.dayCount = Math.floor(Math.random() * 30 + 1);
    },
  },
};
</script>

<style scoped lang="scss">
.page-wrapper {
  .search-pane {
    display: flex;
    justify-content: center;
    border-bottom: 1px solid #dcdfe6;
    margin-bottom: 24px;
  }
}
</style>