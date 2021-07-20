<template>
  <div class="page-wrapper">
    <el-form inline label-position="right" class="search-pane">
      <el-form-item label="市场选择">
        <el-cascader
          collapse-tags
          :options="regionList"
          v-model="searchMarket"
          :props="{ multiple: true }"
          clearable
        />
      </el-form-item>

      <div style="margin-bottom: 20px">
        农产品种类
        <el-select placeholder="请选择" v-model="timeInterval">
          <el-option label="银耳" value="year" />
          <el-option label="金针菇" value="month" />
          <el-option label="胡萝卜" value="day" />
        </el-select>
      </div>

      <el-form-item>
        <el-button type="primary" @click="queryclick">预测</el-button>
      </el-form-item>
    </el-form>

    <div class="block">
      <span class="demonstration">按照该时间段预测 </span>
      <el-date-picker
        v-model="value1"
        type="datetimerange"
        range-separator="至"
        start-placeholder="开始日期"
        end-placeholder="结束日期"
      >
      </el-date-picker>
    </div>
    <br />

    <v-chart class="chart" :option="chartOption" />
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
      timeInterval: null,
      chartOption: {
        backgroundColor: "#000",
        title: {
          text: "农产品价格预测折线图",
          textStyle: {
            color: "#fff",
            fontSize: 18,
            fontWeight: "bold",
          },
          subtext: "已根据您选择的时间段预测价格",
          subtextStyle: {
            color: "#ddd",
          },
        },
        tooltip: {
          show: true,
          trigger: "axis",
          axisPointer: {
            type: "cross",
            crossStyle: {
              color: "#ddd",
            },
          },
        },
        grid: {
          left: 20,
          right: 20,
          top: 80,
          bottom: 20,
          containLabel: true,
        },
        xAxis: {
          show: true,
          axisLabel: {
            interval: 1,
            rotate: -20,
            margin: 30,
            color: "#ddd",
            align: "center",
          },
          axisTick: {
            alignWithLabel: true,
            lineStyle: {
              color: "#ddd",
            },
          },
          data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        },
        yAxis: [
          {
            type: "value",
            name: "￥",
            nameTextStyle: {
              color: "#ddd",
            },
            axisLabel: {
              color: "#ddd",
            },
            axisTick: {
              alignWithLabel: true,
              lineStyle: {
                color: "#ddd",
              },
            },
            splitLine: {
              show: false,
            },
          },
        ],
        series: [
          {
            type: "line",
            name: "测试",
            stack: "人数",
            data: [5, 9, 3, 7, 8, 12, 45, 25, 11, 6, 9, 20],
            label: {
              show: true,
              position: "insideTop",
              offset: [0, 20],
              color: "#000",
            },
            emphasis: {
              label: {
                color: "#fff",
              },
            },
          },
        ],
      },
    };
  },
  methods: {
    queryclick() {
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

  .chart {
    width: 900px;
    height: 500px;
  }
}
</style>