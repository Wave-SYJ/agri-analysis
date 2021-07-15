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
    </div>

    <div class="page-main">
      <el-table :data="tableData">
        <template v-for="(column, index) in columns">
          // index
          <el-table-column
            v-if="column.type === 'index'"
            :key="column.key || column.prop || column.title"
            type="index"
            width="50"
          />

          // date
          <el-table-column
            v-if="column.type === 'date'"
            :key="column.key || column.prop || column.title"
            :label="column.title"
          >
            <template v-slot="scope">
              {{ dayjs(scope.row[column.prop]).format(column.format) }}
            </template>
          </el-table-column>

          // text
          <el-table-column
            v-if="column.type === 'text'"
            :key="column.key || column.prop || column.title"
            :label="column.title"
          >
            <template v-slot="scope">
              {{ scope.row[column.prop] }}
            </template>
          </el-table-column>

          // number
          <el-table-column
            v-if="column.type === 'number'"
            :key="column.key || column.prop || column.title"
            :label="column.title"
          >
            <template v-slot="scope">
              {{ scope.row[column.prop] }} {{ column.suffix }}
            </template>
          </el-table-column>

          // operations
          <el-table-column
            v-if="column.type === 'operations'"
            :key="column.key || column.prop || column.title"
            :label="column.title"
          >
            <template>
              <el-button size="small" type="primary" icon="el-icon-edit"
                >编辑</el-button
              >
              <el-button size="small" type="danger" icon="el-icon-delete"
                >删除</el-button
              >
            </template>
          </el-table-column>
        </template>
      </el-table>
    </div>
  </div>
</template>

<script>
import dayjs from "dayjs";

export default {
  props: {
    tableData: Array,
    columns: Array,
  },
  data() {
    return {
      dayjs,
      editingIndex: null
    };
  },
};
</script>

<style scoped lang="scss">
.page-container {
  display: flex;
  flex-direction: column;

  .page-header {
    flex: none;
    margin-bottom: 10px;
  }

  .page-main {
    flex: auto;
  }
}
</style>