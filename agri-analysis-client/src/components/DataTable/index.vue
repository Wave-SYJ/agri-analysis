<template>
  <div class="page-container">
    <div class="page-header">
      <div class="page-header-left">
        <el-button type="success" icon="el-icon-plus" size="medium">
          添加
        </el-button>
        <el-button type="danger" icon="el-icon-delete" size="medium">
          删除
        </el-button>
      </div>
      <div class="page-header-right">
        <el-button icon="el-icon-search" @click="handleStartSearch"
          >搜索</el-button
        >
      </div>
    </div>

    <div class="page-main">
      <el-table :data="currentData" :height="tableHeight">
        <template v-for="column in columns">
          // index
          <el-table-column
            v-if="column.type === 'index'"
            :key="column.key || column.prop || column.title"
            type="index"
            width="50"
            align="right"
          />

          // date
          <el-table-column
            v-if="column.type === 'date'"
            :key="column.key || column.prop || column.title"
            :label="column.title"
          >
            <template v-slot="scope">
              <span v-if="editingIndex !== scope.$index || !column.editable">
                {{ dayjs(scope.row[column.prop]).format(column.format) }}
              </span>
              <el-date-picker
                v-else
                v-model="editingObj[column.prop]"
                type="date"
                placeholder="选择日期"
              />
            </template>
          </el-table-column>

          // text
          <el-table-column
            v-if="column.type === 'text'"
            :key="column.key || column.prop || column.title"
            :label="column.title"
          >
            <template v-slot="scope">
              <span v-if="editingIndex !== scope.$index || !column.editable">
                {{ scope.row[column.prop] }}
              </span>
              <el-input v-else v-model="editingObj[column.prop]" />
            </template>
          </el-table-column>

          // number
          <el-table-column
            v-if="column.type === 'number'"
            :key="column.key || column.prop || column.title"
            :label="column.title"
          >
            <template v-slot="scope">
              <span v-if="editingIndex !== scope.$index || !column.editable">
                {{ scope.row[column.prop] }} {{ column.suffix }}
              </span>
              <span v-else>
                <el-input-number
                  style="margin-right: 5px"
                  v-model="editingObj[column.prop]"
                  :precision="2"
                  :step="0.1"
                />
                {{ column.suffix }}
              </span>
            </template>
          </el-table-column>

          // options
          <el-table-column
            v-if="column.type === 'select'"
            :key="column.key || column.prop || column.title"
            :label="column.title"
          >
            <template v-slot="scope">
              <span v-if="editingIndex !== scope.$index || !column.editable">
                {{
                  column.options.find(
                    (option) => option.value === scope.row[column.prop]
                  ).title
                }}
              </span>
              <el-select
                v-else
                v-model="editingObj[column.prop]"
                placeholder="请选择"
              >
                <el-option
                  v-for="option in column.options"
                  :key="option.value"
                  :label="option.title"
                  :value="option.value"
                >
                </el-option>
              </el-select>
            </template>
          </el-table-column>

          // operations
          <el-table-column
            v-if="column.type === 'operations'"
            :key="column.key || column.prop || column.title"
            :label="column.title"
            :width="250"
          >
            <template v-slot="scope">
              <el-button
                v-if="editingIndex !== scope.$index"
                :disabled="editingIndex !== null"
                size="small"
                type="primary"
                icon="el-icon-edit"
                @click="handleStartEdit(scope.$index, scope.row)"
              >
                编辑
              </el-button>
              <template v-else>
                <el-button size="small" type="primary" icon="el-icon-check">
                  确定
                </el-button>
                <el-button
                  @click="handleCancelEdit"
                  size="small"
                  icon="el-icon-close"
                >
                  取消
                </el-button>
              </template>

              <el-button
                v-if="editingIndex !== scope.$index"
                :disabled="editingIndex !== null"
                size="small"
                type="danger"
                icon="el-icon-delete"
              >
                删除
              </el-button>
            </template>
          </el-table-column>
        </template>
      </el-table>
    </div>

    <el-drawer
      title="高级搜索"
      :visible.sync="searchDrawerShow"
      direction="rtl"
    >
      <el-form
        label-position="right"
        label-width="80px"
        style="margin-right: 30px"
      >
        <template v-for="column in columns">
          <el-form-item
            :key="column.key || column.prop || column.title"
            :label="column.title"
            v-if="column.type === 'text'"
          >
            <el-input v-model="searchObj[column.prop]" />
          </el-form-item>
          <el-form-item
            :key="column.key || column.prop || column.title"
            :label="column.title"
            v-else-if="column.type === 'date'"
          >
            <el-date-picker
              v-model="searchObj[column.prop]"
              type="daterange"
              range-separator="至"
              start-placeholder="开始日期"
              end-placeholder="结束日期"
            >
            </el-date-picker>
          </el-form-item>
          <el-form-item
            :key="column.key || column.prop || column.title"
            :label="column.title"
            v-if="column.type === 'number'"
          >
            <NumberRangeInput v-model="searchObj[column.prop]" />
          </el-form-item>
        </template>
      </el-form>
    </el-drawer>

    <div class="page-footer">
      <el-pagination
        class="page-footer-pagination"
        :current-page="currentPage"
        :page-sizes="[100, 200, 300, 400]"
        :page-size="100"
        layout="total, sizes, prev, pager, next, jumper"
        :total="400"
      >
      </el-pagination>
    </div>
  </div>
</template>

<script>
import dayjs from "dayjs";
import NumberRangeInput from '@/components/NumberRangeInput'

export default {
  props: {
    tableData: Array,
    columns: Array,
  },
  components: {
    NumberRangeInput
  },
  data() {
    return {
      dayjs,
      editingIndex: null,
      editingObj: {},
      currentPage: 1,
      documentHeight: document.documentElement.clientHeight,

      searchDrawerShow: false,
      searchObj: {},
      currentData: [],
    };
  },
  methods: {
    handleStartEdit(index, obj) {
      this.editingIndex = index;
      this.editingObj = { ...obj };
    },
    handleCancelEdit() {
      this.editingIndex = null;
      this.editingObj = {};
    },
    handleStartSearch() {
      this.searchDrawerShow = true;
    },
    getSearchInitObj() {
      const result = {};
      this.columns
        .filter((column) => column.searchable)
        .forEach((column) => {
          switch (column.type) {
            case "text":
              result[column.prop] = "";
              break;
            case "date":
              result[column.prop] = [null, null];
              break;
            case "number":
              result[column.prop] = [null, null];
              break;
            default:
              result[column.prop] = null;
              break;
          }
        });
      return result;
    },
  },
  mounted() {
    this.currentData = this.tableData;
    window.onresize = () =>
      (this.documentHeight = document.documentElement.clientHeight);
  },
  computed: {
    tableHeight() {
      return Math.max(this.documentHeight - 258, 400);
    },
  },
  created() {
    this.searchObj = this.getSearchInitObj()
  }
};
</script>

<style scoped lang="scss">
.page-container {
  display: flex;
  flex-direction: column;

  .page-header {
    flex: none;
    margin-bottom: 10px;
    display: flex;
    .page-header-right {
      margin-left: auto;
    }
  }

  .page-main {
    flex: auto;
  }

  .page-footer {
    flex: none;
    display: flex;
    margin-top: 15px;

    .page-footer-pagination {
      margin-left: auto;
    }
  }
}
</style>