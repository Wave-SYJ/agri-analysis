<template>
  <DataTable :tableData="tableData" :totalItems="totalItmes" :columns="columns" @insert="handleInsert" :loading="!!loading" @delete="handleDelete" @update="handleUpdate" @refresh="handleRefresh" />
</template>

<script>
import DataTable from "@/components/DataTable"
import { getProductList, insertProduct, deleteProducts, updateProduct } from '@/api/product'
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
    async handleRefresh(pagination) {
      this.loading++;
      const res = await getProductList(pagination.pageNo, pagination.pageSize);
      this.pagination = pagination
      this.tableData = res.list;
      this.totalItmes = res.total;
      this.loading--;
    },
    async handleInsert(data) {
      this.loading++;
      await insertProduct(data)
      this.handleRefresh(this.pagination);
      this.loading--;
    },
    async handleDelete(list) {
      this.loading++;
      await deleteProducts(list);
      this.handleRefresh(this.pagination);
      this.loading--;
    },
    async handleUpdate(data) {
      this.loading++;
      await updateProduct(data);
      this.handleRefresh(this.pagination);
      this.loading--;
    }
  },
}
</script>

<style>

</style>