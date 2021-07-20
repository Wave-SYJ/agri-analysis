<template>
  <div class="page-wrapper">
    <div class="page-header">
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
          <el-button type="primary">查询</el-button>
        </el-form-item>
      </el-form>
    </div>

    <div class="page-main">
      <v-chart autoresize :option="chartOption" />
    </div>
  </div>
</template>

<script>
import * as echarts from "echarts";
import regionList from "./fakeRegionData";

export default {
  data() {
    return {
      regionList,
      searchType: null,
      searchMarket: null,

      chartOption: {
        backgroundColor: "#FFFFFF",
        title: {
          top: 20,
          text: "品种对比",
          family: "微软雅黑",
          fontWeight: "normal",
          fontSize: 30,
          color: "#777879",
          //align: center
          left: "40%",
        },
        //提示框组件
        tooltip: {
          trigger: "axis", //坐标轴触发
          axisPointer: {
            lineStyle: {
              color: "#EAB543",
            },
          },
        },
        //图例
        legend: {
          top: 20,
          icon: "rect",
          itemWidth: 14,
          itemHeight: 7,
          itemGap: 13, //间隔
          data: ["A 品种", "B 品种"],
          right: "4%",
          textStyle: {
            fontSize: 20,
            color: "#73716D",
          },
        },
        //网格
        grid: {
          top: 100,
          left: "2%",
          right: "2%",
          bottom: "2%",
          containLabel: true, //grid区域是否包含刻度标签
        },
        xAxis: [
          {
            type: "category",
            boundaryGap: false,
            axisLine: {
              lineStyle: {
                color: "#6F7072",
              },
              axisLabel: {
                margin: 10,
                textStyle: {
                  fontSize: 20,
                },
              },
            },
            data: ["7-16", "7-17", "7-18", "7-19", "7-20"],
          },
        ],
        yAxis: [
          {
            type: "value",
            name: "(元/斤)",
            axisTick: {
              show: false,
            },
            axisLine: {
              lineStyle: {
                color: "#6F7072",
              },
            },
            axisLabel: {
              margin: 10,
              textStyle: {
                fontSize: 20,
              },
            },
            splitLine: {
              lineStyle: {
                color: "#6F7072",
              },
            },
          },
        ],
        series: [
          {
            name: "A 品种",
            type: "line",
            smooth: false,
            symbol: "circle",
            symbolSize: 5,
            showSymbol: false,
            lineStyle: {
              width: 1,
            },
            //区域填充样式
            areaStyle: {
              color: new echarts.graphic.LinearGradient(
                0,
                0,
                0,
                1,
                [
                  {
                    offset: 0,
                    color: "rgba(137, 189, 27, 0.3)",
                  },
                  {
                    offset: 0.8,
                    color: "rgba(137, 189, 27, 0)",
                  },
                ],
                false
              ),
              shadowColor: "rgba(0, 0, 0, 0.1)",
              shadowBlur: 10,
            },
            itemStyle: {
              color: "rgb(137,189,27)",
              borderColor: "rgba(137,189,2,0.27)",
              borderWidth: 12,
            },
            data: [220, 182, 191, 134, 150],
          },
          {
            name: "B 品种",
            type: "line",
            smooth: false,
            symbol: "circle",
            symbolSize: 5,
            showSymbol: false,
            lineStyle: {
              width: 1,
            },
            areaStyle: {
              color: new echarts.graphic.LinearGradient(
                0,
                0,
                0,
                1,
                [
                  {
                    offset: 0,
                    color: "rgba(0, 136, 212, 0.3)",
                  },
                  {
                    offset: 0.8,
                    color: "rgba(0, 136, 212, 0)",
                  },
                ],
                false
              ),
              shadowColor: "rgba(0, 0, 0, 0.1)",
              shadowBlur: 10,
            },
            itemStyle: {
              color: "rgb(0,136,212)",
              borderColor: "rgba(0,136,212,0.2)",
              borderWidth: 12,
            },
            data: [120, 110, 125, 145, 122],
          },
        ],
      },
    };
  },
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