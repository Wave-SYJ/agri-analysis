<template>
  <div>
    <div class="fragment basic-info-fragment">
      <div class="fragment-header">基本信息</div>
      <div class="fragment-body" v-loading="!!basicInfoLoading">
        <div class="fragment-body-item">
          <div class="fragment-body-item-key">
            <i class="el-icon-school" style="color: rgba(248, 123, 6, 0.5)" />
            <span class="fragment-body-item-key-text">市场总数</span>
          </div>
          <div
            class="fragment-body-item-value"
            style="color: rgba(248, 123, 6, 0.5)"
          >
            {{ basicInfo.marketTotal }}
          </div>
        </div>
        <div class="fragment-body-item">
          <div class="fragment-body-item-key">
            <i class="el-icon-orange" style="color: rgba(6, 187, 15, 0.411)" />
            <span class="fragment-body-item-key-text">品种总数</span>
          </div>
          <div
            class="fragment-body-item-value"
            style="color: rgba(6, 187, 15, 0.411)"
          >
            {{ basicInfo.typeTotal }}
          </div>
        </div>
        <div class="fragment-body-item">
          <div class="fragment-body-item-key">
            <i
              class="el-icon-watermelon"
              style="color: rgba(214, 53, 4, 0.411)"
            />
            <span class="fragment-body-item-key-text">种类总数</span>
          </div>
          <div
            class="fragment-body-item-value"
            style="color: rgba(214, 53, 4, 0.411)"
          >
            {{ basicInfo.varietyTotal }}
          </div>
        </div>
        <div class="fragment-body-item">
          <div class="fragment-body-item-key">
            <i
              class="el-icon-document-checked"
              style="color: rgba(6, 186, 218, 0.507)"
            />
            <span class="fragment-body-item-key-text">总抓取量</span>
          </div>
          <div
            class="fragment-body-item-value"
            style="color: rgba(6, 186, 218, 0.507)"
          >
            {{ basicInfo.productTotal }}
          </div>
        </div>
      </div>
    </div>

    <div class="fragment data-monitor-fragment" style="margin-top: 20px">
      <div class="fragment-header">数据监控</div>
      <div class="fragment-body">
        <div class="fragment-body-header">
          <i class="el-icon-position fragment-body-header-icon" />
          <span class="fragment-body-header-title">抓取量查询</span>
        </div>
        <el-divider style="font-color=rgba(0, 0, 0, 0.200);"></el-divider>
        <div class="fragment-body-main">
          <el-form
            inline
            label-position="right"
            class="fragment-body-search-pane"
          >
            <el-form-item label="地区">
              <el-cascader
                :value="searchMarket"
                :props="{
                  lazy: true,
                  lazyLoad: loadMarketCascade,
                }"
              />
            </el-form-item>
            <el-form-item>
              <el-button type="primary" icon="el-icon-search">查询</el-button>
            </el-form-item>
          </el-form>
          <div class="fragment-body-charts">
            <v-chart
              autoresize
              class="fragment-body-line-chart"
              :option="lineChartOption"
            />
            <v-chart
              autoresize
              class="fragment-body-pie-chart"
              :option="pieChartOption"
            />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import * as echarts from "echarts";
import { getBasicInfo } from "@/api/monitor";
import {
  getProvinceList,
  getMarketList,
  getCityList,
} from "@/api/category";

export default {
  data() {
    return {
      basicInfo: {},
      basicInfoLoading: 0,

      searchMarket: null,
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

      lineChartOption: {
        backgroundColor: "#FFFFFF",
        title: {
          top: 20,
          text: "抓取数量",
          textStyle: {
            family: "微软雅黑",
            fontWeight: "normal",
            fontSize: 30,
            color: "#777879",
            //align: center
          },
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
          data: ["果品", "其他"],
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
                fontSize: 20,
              },
            },
            data: ["7-16", "7-17", "7-18", "7-19", "7-20"],
          },
        ],
        yAxis: [
          {
            type: "value",
            name: "(条)",
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
              fontSize: 20,
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
            name: "果品",
            type: "line",
            smooth: true,
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
            name: "其他",
            type: "line",
            smooth: true,
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
      pieChartOption: {
        title: {
          text: "所占记录数",
          subtext: "纯属虚构",
          left: "center",
        },
        tooltip: {
          trigger: "item",
        },
        legend: {
          orient: "vertical",
          left: "left",
        },
        series: [
          {
            name: "访问来源",
            type: "pie",
            radius: "50%",
            data: [
              { value: 1048, name: "果品" },
              { value: 735, name: "其他" },
            ],
            emphasis: {
              itemStyle: {
                shadowBlur: 10,
                shadowOffsetX: 0,
                shadowColor: "rgba(0, 0, 0, 0.5)",
              },
            },
          },
        ],
      },
    };
  },
  async created() {
    this.basicInfoLoading++;
    this.basicInfo = await getBasicInfo();
    this.basicInfoLoading--;
  },
  methods: {
    loadMarketCascade(node, resolve) {
      this.getMarketOptionsFuns[node.level](node.value).then((res) =>
        resolve(res)
      );
    },
  },
};
</script>

<style scoped lang="scss">
.fragment {
  .fragment-header {
    font-size: 32px;
    color: rgba(0, 0, 0, 0.658);
    font-family: "微软雅黑";
    font-weight: 600;
    margin-bottom: 10px;
  }

  .fragment-body {
    font-size: 12px;
    box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
    padding: 20px;
  }
}

.fragment.basic-info-fragment {
  .fragment-body {
    display: flex;

    .fragment-body-item {
      flex: auto;
      .fragment-body-item-key {
        font-size: 30px;
        font-family: "微软雅黑";
        font-weight: 500;
        text-align: center;
        margin-bottom: 20px;

        .fragment-body-item-key-text {
          margin-left: 10px;
          color: rgba(0, 0, 0, 0.438);
          font-size: 20px;
          line-height: 40px;
          vertical-align: top;
        }
      }

      .fragment-body-item-value {
        font-size: 40px;
        font-family: "微软雅黑";
        font-weight: 600;
        text-align: center;
      }
    }
  }
}

.fragment.data-monitor-fragment {
  .fragment-body {
    .fragment-body-header {
      .fragment-body-header-icon {
        margin-left: 30px;
        color: rgba(0, 132, 255, 0.61);
        font-size: 30px;
      }
      .fragment-body-header-title {
        margin-left: 10px;
        vertical-align: super;
        color: rgba(0, 0, 0, 0.459);
        font-size: 23px;
      }
    }

    .fragment-body-main {
      display: flex;
      flex-direction: column;
      align-items: center;

      .fragment-body-charts {
        display: flex;
        margin-top: 10px;
        justify-content: space-evenly;
        width: 100%;

        .fragment-body-line-chart {
          height: 500px;
          width: 500px;
          flex: none;
        }

        .fragment-body-pie-chart {
          height: 500px;
          width: 500px;
          flex: none;
        }
      }
    }
  }
}
</style>