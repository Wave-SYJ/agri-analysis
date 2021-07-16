<template>
  <div>
    <el-row style="margin-top:30px">
      <span style="color: #409eff">请选择省</span>
      <span style="margin-left: 130px; color: #409eff">请选择市</span>
      <span style="margin-left: 130px; color: #409eff">请选择市场</span>
      <span style="margin-left: 130px; color: #409eff">请选择农产品种类</span>
    </el-row>
    <el-row>
      <el-select v-model="value1" change="province_select" placeholder="请选择">
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        >
        </el-option>
      </el-select>

      <el-select
        v-model="value2"
        change="city_select"
        collapse-tags
        style="margin-left: 64px"
        placeholder="请选择"
      >
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        >
        </el-option>
      </el-select>
      <el-select
        v-model="value3"
        change="market_select"
        collapse-tags
        style="margin-left: 64px"
        placeholder="请选择"
      >
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        >
        </el-option>
      </el-select>
      <el-select
        v-model="value4"
        collapse-tags
        style="margin-left: 80px"
        placeholder="请选择"
      >
        <el-option
          v-for="item in options"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        >
        </el-option>
      </el-select>
      <el-button
        round
        style="margin-left: 64px; color: white; background-color: #67c23a"
        @click="queryclick"
        >查询售卖行情</el-button
      >
    </el-row>
    <el-row class="a">
      <span style="color: ##67c23a">您查询的农作物数据天数为:</span
      ><span style="color: #409eff">{{ x }}</span>
    </el-row>
    <el-row class="b"
      ><span style="color: #409eff">请选择行情显示时间间隔</span>
      <el-select
        style="margin-left: 20px"
        v-model="timespan"
        placeholder="请选择"
      >
        <el-option
          v-for="item in time_span"
          :key="item.value"
          :label="item.label"
          :value="item.value"
        >
        </el-option>
      </el-select>
      <el-button
        round
        style="margin-left: 64px; color: white; background-color: #409eff"
        @click="displaychart">显示图表</el-button>
    </el-row>
    <div id="echarts_b_c" class="echarts"></div>
  </div>
</template>
 



<script>
export default {
  data() {
    return {
      options: [
        {
          value: "选项1",
          label: "黄金糕",
        },
        {
          value: "选项2",
          label: "双皮奶",
        },
        {
          value: "选项3",
          label: "蚵仔煎",
        },
        {
          value: "选项4",
          label: "龙须面",
        },
        {
          value: "选项5",
          label: "北京烤鸭",
        },
      ],
      time_span: [
        {
          value: "年",
          label: "年",
        },
        {
          value: "月",
          label: "月",
        },
        {
          value: "日",
          label: "日",
        },
      ],
      value1: null,
      value2: null,
      value3: null,
      value4: null,
      timespan: null,
      x: null,
      xAxisData: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
      dataTest: [5, 9, 3, 7, 8, 12, 45, 25, 11, 6, 9, 20],
    };
  },

  mounted() {
    this.drowLine();
  },

  methods: {
    queryclick() {
      this.x = console.log(this.value1);
    },
    displaychart() {},
    province_select() {},
    city_select() {},
    market_select() {},
    drowLine() {
      let echarts = this.$echarts.init(document.getElementById("echarts_b_c"));
      echarts.setOption({
        backgroundColor: "#000",
        title: {
          text: "农产品售卖行情",
          textStyle: {
            color: "#fff",
            fontSize: 18,
            fontWeight: "bold",
          },
          subtext: "已根据您选择的时间间隔显示图表",
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
            textStyle: {
              color: "#ddd",
              align: "center",
            },
          },
          axisTick: {
            alignWithLabel: true,
            lineStyle: {
              color: "#ddd",
            },
          },
          data: this.xAxisData,
        },
        yAxis: [
          {
            type: "value",
            name: "(人/次)",
            nameTextStyle: {
              color: "#ddd",
            },
            axisLabel: {
              textStyle: {
                color: "#ddd",
              },
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
            data: this.dataTest,
            label: {
              normal: {
                show: true,
                position: "insideTop",
                offset: [0, 20],
                textStyle: {
                  color: "#000",
                },
              },
              emphasis: {
                textStyle: {
                  color: "#fff",
                },
              },
            },
          },
        ],
      });
    },
  },
};
</script>

<style>
.el-select .el-input {
  width: 130px;
}
.input-with-select .el-input-group__prepend {
  background-color: #fff;
}
.text {
  -moz-column-count: 4; /* Firefox */
  column-count: 4;
}
.a {
  width: 100%;
  height: 50px;
  margin-top: 50px;
}
.b {
  width: 100%;
  height: 100px;
  margin-top: 25px;
}
.echarts {
  width: 900px;
  height: 500px;
  background-color: #fff;
  margin: 5px;
}
</style>
