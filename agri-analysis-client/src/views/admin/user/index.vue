<template>
  <DataTable :tableData="tableData" :columns="columns" @insert="handleInsert" :loading="!!loading" />
</template>

<script>
import DataTable from "@/components/DataTable"
import { getAdminList, insertAdmin } from '@/api/admin'
import columns from './columns'

export default {
  components: {
    DataTable
  },
  data() {
    return {
      tableData: [],
      columns,
      loading: 0
    }
  },
  methods: {
    async refreshDataList() {
      this.loading++;
      this.tableData = await getAdminList();
      this.loading--;
    },
    async handleInsert(data) {
      this.loading++;
      await insertAdmin(data)
      this.refreshDataList();
      this.loading--;
    }
  },
  created() {
    this.refreshDataList()
  }
}
</script>

<style>

</style>