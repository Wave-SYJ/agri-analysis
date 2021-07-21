<template>
  <div class="page-wrapper">
    <div class="page-header">
      <el-form inline label-position="right" class="search-pane">
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
          <el-button type="primary">查询</el-button>
        </el-form-item>
      </el-form>
    </div>

    <div class="page-main">
      <div class="page-main-left">
        <v-chart autoresize :option="leftOptions" />
      </div>
      <div class="page-main-right">
        <Map />
      </div>
    </div>
  </div>
</template>

<script>
import regionList from "./fakeRegionData";
import Map from '@/components/Map'

export default {
  components: {
    Map
  },
  data() {
    return {
      regionList,

      searchType: null,

      leftOptions: {
        title: {
          text: "富士苹果区域行情",
          subtext: "数据来自网络",
        },
        xAxis: {
          type: "value",
        },
        yAxis: {
          type: "category",
          data: [
            "北京",
            "天津",
            "河北",
            "山西",
            "内蒙古",
            "辽宁",
            "吉林",
            "浙江",
            "安徽",
          ],
        },
        series: [
          {
            data: [1.2, 2, 1.5, 0.8, 0.7, 1.1, 1.3, 1.2, 0.9],
            type: "bar",
          },
        ],
      },
    };
  },
  methods: {},
};
</script>

<style lang="scss" scoped>
.page-wrapper {
  display: flex;
  height: 100%;
  flex-direction: column;

  .page-header {
    display: flex;
    flex: none;
    justify-content: center;
    border-bottom: 1px solid #dcdfe6;
    margin-bottom: 20px;
  }

  .page-main {
    flex: auto;
    display: flex;
    .page-main-left {
      width: 500px;
      height: 100%;
      flex: none;
    }
    .page-main-right {
      flex: auto;
    }
  }
}
</style>