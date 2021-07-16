<template>
  <div>
    <span class="biaoti">
      <br />
      &emsp;<i class="el-icon-ship" style="color: rgba(0, 132, 255, 0.61)"></i
      >&#32; 品种对比 <br />
      <br />
    </span>
    <div style="box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1)">
      <!-- <div> -->
      <ul class="demo" style="text-align: center">
        <el-form ref="form" :model="form" label-width="80px">
          <li>
            <br />
            <br />
            <el-form-item label="省份" class="biaodan">
              <el-select v-model="form.province" placeholder="请选择省份">
                <el-option label="北京市" value="北京市"></el-option>
                <el-option label="上海市" value="上海市"></el-option>
              </el-select>
              <br />
            </el-form-item>
          </li>

          <li>
            <br />
            <el-form-item label="批发市场" class="biaodan">
              <el-select v-model="form.market" placeholder="请选择批发市场">
                <el-option label="a" value="shanghai"></el-option>
                <el-option label="b" value="beijing"></el-option>
              </el-select>
              <br />
            </el-form-item>
          </li>

          <li>
            <br />
            <el-form-item label="产品类别" class="biaodan">
              <el-select v-model="form.type" placeholder="请选择产品类别">
                <el-option label="北京市" value="北京市"></el-option>
                <el-option label="上海市" value="上海市"></el-option>
              </el-select>
              <br />
            </el-form-item>
          </li>

          <!-- </div> -->
          <br />

          <el-form-item>
            <br />
            <br />
            <el-button type="primary" @click="onSubmit" icon="el-icon-search"
              >开始查询</el-button
            >
          </el-form-item>
          <br /><br />
        </el-form>
      </ul>
      <br />
      <el-divider style="font-color=rgba(0, 0, 0, 0.200);"></el-divider>
      <img src="#" />
      <img src="#" />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      // value1: '',
      // value2: '',
      // value3: '',
      // value4: '',
      form: {
        province: "",
        market: "",
        type: "",
        //   variety: ''
      },
    };
  },
  methods: {
    onSubmit() {
      console.log("submit!");
    },
  },
};
</script>

<style>
.biaoti {
  font-size: 32px;
  color: rgba(0, 0, 0, 0.658);
  font-family: "微软雅黑";
  font-weight: 600;
}

.demo {
  column-count: 2;
  column-rule: 3px solid rgb(255, 255, 255);
  font-size: 12px;
  /* box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1); */
}

.demo li {
  list-style: none;
}

.biaodan {
  font-size: 18px;
  color: rgba(0, 0, 0, 0.658);
  font-family: "微软雅黑";
}
</style>