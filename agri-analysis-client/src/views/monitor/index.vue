<template>
  <div>
    <div class="fragment basic-info-fragment">
      <div class="fragment-header">基本信息</div>
      <div class="fragment-body">
        <div class="fragment-body-item">
          <div class="fragment-body-item-key">
            <i class="el-icon-school" style="color: rgba(248, 123, 6, 0.5)" />
            <span class="fragment-body-item-key-text">市场总数</span>
          </div>
          <div
            class="fragment-body-item-value"
            style="color: rgba(248, 123, 6, 0.5)"
          >
            123
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
            123
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
            123
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
            123
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
              <el-button
                type="primary"
                icon="el-icon-search"
                @click="queryclick"
                >查询</el-button
              >
            </el-form-item>
          </el-form>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import regionList from "./fakeRegionData";
export default {
  data() {
    return {
      regionList,
    };
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
    }
  }
}
</style>