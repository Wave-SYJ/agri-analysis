<template>
  <div>
    <span class="biaoti">
      <br />
      &emsp;基本信息 <br />
      <br />
    </span>
    <ul class="demo">
      <li>
        <br />
        <i class="el-icon-school" style="color: rgba(248, 123, 6, 0.5)"></i>
        <span class="demonstration">&emsp;市场总数<br /><br /> </span>
      </li>
      <li>
        <span class="data" style="color: rgba(248, 123, 6, 0.5)"
          >&emsp;&emsp;123<br /><br />
        </span>
      </li>

      <li>
        <br />
        <i class="el-icon-orange" style="color: rgba(6, 187, 15, 0.411)"></i>
        <span class="demonstration">&emsp;品种总数<br /><br /> </span>
      </li>
      <li>
        <span class="data" style="color: rgba(6, 187, 15, 0.411)"
          >&emsp;&emsp;1234<br /><br />
        </span>
      </li>

      <li>
        <br />
        <i
          class="el-icon-watermelon"
          style="color: rgba(214, 53, 4, 0.411)"
        ></i>
        <span class="demonstration">&emsp;种类总数<br /><br /> </span>
      </li>
      <li>
        <span class="data" style="color: rgba(214, 53, 4, 0.411)"
          >&emsp;&emsp;12345<br /><br />
        </span>
      </li>

      <li>
        <br />
        <i
          class="el-icon-document-checked"
          style="color: rgba(6, 186, 218, 0.507)"
        ></i>
        <span class="demonstration">&emsp;总抓取量<br /><br /> </span>
      </li>
      <li>
        <span class="data" style="color: rgba(6, 186, 218, 0.507)"
          >&emsp;&emsp;123456<br /><br />
        </span>
      </li>
    </ul>

    <span class="biaoti">
      <br />
      &emsp;数据监控 <br />
      <br />
    </span>
    <div style="box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1)">
      <span style="color: rgba(0, 0, 0, 0.459); font-size: 23px"
        ><br />&emsp;&emsp;
        <i class="el-icon-position" style="color: rgba(0, 132, 255, 0.61)"></i>
        &#32;&#32; 抓取量查询</span
      >
      <el-divider style="font-color=rgba(0, 0, 0, 0.200);"></el-divider>
      <br /><br />
      <!-- <div> -->
      <ul class="demo2" style="text-align: center">
        <el-form ref="form" :model="form" label-width="80px">
          <li>
            <el-form-item label="省份">
              <el-select v-model="form.province" placeholder="请选择省份">
                <el-option label="北京市" value="北京市"></el-option>
                <el-option label="上海市" value="上海市"></el-option>
              </el-select>
            </el-form-item>
          </li>

          <li>
            <el-form-item label="批发市场">
              <el-select v-model="form.market" placeholder="请选择批发市场">
                <el-option label="a" value="shanghai"></el-option>
                <el-option label="b" value="beijing"></el-option>
              </el-select>
            </el-form-item>
          </li>

          <li>
            <el-form-item label="产品种类">
              <el-select v-model="form.type" placeholder="请选择产品种类">
                <el-option label="a" value="shanghai"></el-option>
                <el-option label="b" value="beijing"></el-option>
              </el-select>
            </el-form-item>
          </li>

          <li>
            <el-form-item>
              <el-button type="primary" @click="onSubmit" icon="el-icon-search"
                >开始查询</el-button
              >
            </el-form-item>
          </li>
          <!-- </div> -->
          <br /><br />
          <br /><br />
          <br /><br />
        </el-form>
      </ul>
      <img src="#" />
      <img src="#" />
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        province: "",
        market: "",
        type: "",
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
.white {
  background-color: rgb(255, 255, 255);
}

.demonstration {
  font-size: 20px;
  color: rgba(0, 0, 0, 0.438);
  font-family: "微软雅黑";
  font-weight: 500;
  text-align: center;
}
.data {
  font-size: 40px;
  /* color:rgba(0, 0, 0, 0.637); */
  font-family: "微软雅黑";
  font-weight: 600;
  text-align: center;
}
.demo {
  /*列数目*/
  column-count: 4;
  /*列之间分割线宽度，风格，颜色*/
  column-rule: 3px solid rgb(255, 255, 255);
  font-size: 12px;
  box-shadow: 0 2px 12px 0 rgba(0, 0, 0, 0.1);
}
.demo2 {
  /*列数目*/
  column-count: 4;
  /*列之间分割线宽度，风格，颜色*/
  column-rule: 3px solid rgb(255, 255, 255);
  font-size: 12px;
}
.demo2 li {
  list-style: none;
}
.demo li {
  list-style: none;
}
.el-icon-school {
  font-size: 30px;
  color: rgba(0, 0, 0, 0.541);
}
.el-icon-orange {
  font-size: 30px;
  color: rgba(0, 0, 0, 0.541);
}
.el-icon-watermelon {
  font-size: 30px;
  color: rgba(0, 0, 0, 0.541);
}
.el-icon-document-checked {
  font-size: 30px;
  color: rgba(0, 0, 0, 0.541);
}
</style>