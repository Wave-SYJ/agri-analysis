<template>
  <DataTable :tableData="tableData" :totalItems="totalItmes" :columns="columns" @insert="handleInsert" :loading="!!loading" @delete="handleDelete" @update="handleUpdate" @refresh="handleRefresh" :allowEdit="true" />
</template>

<script>
import DataTable from "@/components/DataTable"
import { getAdminList, insertAdmin, deleteAdmins, updateAdmin } from '@/api/admin'
import columns from './columns'

export default {
  components: {
    DataTable
  },
  data() {
    return {
      tableData: [],
      columns,
      loading: 0,
      totalItmes: 0,
      pagination: {}
    }
  },
  methods: {
    async handleRefresh(pagination, sortInfo, searchObj) {
      this.loading++;
      const res = await getAdminList(pagination, sortInfo, searchObj);
      this.pagination = pagination
      this.tableData = res.list;
      this.totalItmes = res.total;
      this.loading--;
    },
    async handleInsert(data) {
      this.loading++;
      await insertAdmin(data)
      this.handleRefresh(this.pagination);
      this.loading--;
    },
    async handleDelete(list) {
      this.loading++;
      await deleteAdmins(list);
      this.handleRefresh(this.pagination);
      this.loading--;
    },
    async handleUpdate(data) {
      this.loading++;
      await updateAdmin(data);
      this.handleRefresh(this.pagination);
      this.loading--;
    }
  },
}
</script>

<style>

</style>