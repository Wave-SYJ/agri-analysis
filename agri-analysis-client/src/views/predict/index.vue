<template>
  <div class="page-wrapper">
    <el-form inline label-position="right" class="search-pane">
      <el-form-item label="按照该时间段预测">
        <el-date-picker
          v-model="dateRange"
          type="daterange"
          range-separator="至"
          start-placeholder="开始日期"
          end-placeholder="结束日期"
        >
        </el-date-picker>
      </el-form-item>
      <el-form-item label="地区">
        <el-cascader
          v-model="searchMarket"
          :props="{
            lazy: true,
            lazyLoad: loadMarketCascade,
          }"
        />
      </el-form-item>

      <el-form-item label="种类">
        <el-cascader
          v-model="searchType"
          :props="{
            lazy: true,
            lazyLoad: loadTypeCascade,
          }"
        />
      </el-form-item>

      <el-form-item>
        <el-button
          type="primary"
          @click="handleQuery"
          :loading="!!searchLoading"
          >预测</el-button
        >
      </el-form-item>
    </el-form>

    <v-chart autoresize class="chart" :option="chartOption" />
  </div>
</template>

<script>
import {
  getProvinceList,
  getMarketList,
  getCityList,
  getTypeList,
  getVarietyList,
} from "@/api/category";
import chartOption from "./chartOption";
import { getPredictData } from "@/api/predict";
import dayjs from 'dayjs';

export default {
  data() {
    return {
      searchMarket: null,
      searchType: null,
      dateRange: null,
      searchLoading: 0,
      getTypeOptionsFuns: [
        async () =>
          (await getTypeList()).map((item) => ({
            label: item.name,
            value: item.id,
            leaf: false,
          })),
        async (typeId) =>
          (await getVarietyList(typeId)).map((item) => ({
            label: item.name,
            value: item.id,
            leaf: true,
          })),
      ],
      getMarketOptionsFuns: [
        async () =>
          (await getProvinceList()).map((item) => ({
            label: item.name,
            value: item.id,
            leaf: false,
          })),
        async (provinceId) =>
          (await getCityList(provinceId)).map((item) => ({
            label: item.name,
            value: item.id,
            leaf: false,
          })),
        async (cityId) =>
          (await getMarketList(cityId)).map((item) => ({
            label: item.name,
            value: item.id,
            leaf: true,
          })),
      ],

      chartOption,
    };
  },
  methods: {
    loadTypeCascade(node, resolve) {
      this.getTypeOptionsFuns[node.level](node.value).then((res) =>
        resolve(res)
      );
    },
    loadMarketCascade(node, resolve) {
      this.getMarketOptionsFuns[node.level](node.value).then((res) =>
        resolve(res)
      );
    },
    async handleQuery() {
      if (this.dateRange === null || this.dateRange.length === 0)
        return this.$message.error("日期范围不能为空");
      if (this.searchMarket === null || this.searchMarket.length === 0)
        return this.$message.error("市场不能为空");
      if (this.searchType === null || this.searchType.length === 0)
        return this.$message.error("种类不能为空");
      console.log(
        await getPredictData(
          this.dateRange.map(item => dayjs(item).format('YYYY-MM-DD')),
          this.searchMarket[2],
          this.searchType[1]
        )
      );
    },
  },
};
</script>

<style scoped lang="scss">
.page-wrapper {
  height: 100%;
  display: flex;
  flex-direction: column;

  .search-pane {
    flex: none;
    display: flex;
    justify-content: center;
    border-bottom: 1px solid #dcdfe6;
    margin-bottom: 24px;
  }

  .chart {
    width: 100%;
    flex: auto;
  }
}
</style>