<template>
  <div>
    <el-row style="margin-top: 30px">
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
        @click="displaychart"
        >显示图表</el-button
      >
    </el-row>
    <img style="margin-top: 10px" src="paris.jpg" alt="绘制" />
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
    };
  },
  methods: {
    queryclick() {
      this.x = console.log(this.value1);
    },
    displaychart() {},
    province_select() {},
    city_select() {},
    market_select() {},
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
</style>