<template>
  <DataTable
    :tableData="tableData"
    :totalItems="totalItmes"
    :columns="columns"
    @insert="handleInsert"
    :loading="!!loading"
    @delete="handleDelete"
    @update="handleUpdate"
    @refresh="handleRefresh"
  />
</template>

<script>
import DataTable from "@/components/DataTable";
import {
  getProductList,
  insertProduct,
  deleteProducts,
  updateProduct,
} from "@/api/product";
import columns from "./columns";
import dayjs from "dayjs";

export default {
  components: {
    DataTable,
  },
  data() {
    return {
      tableData: [],
      columns,
      loading: 0,
      totalItmes: 0,
      pagination: {},
    };
  },
  methods: {
    async handleRefresh(pagination, sortInfo, searchObj) {
      this.loading++;
      if (searchObj) {
        if (
          searchObj.date instanceof Array &&
          searchObj.date[0] &&
          searchObj.date[1]
        )
          searchObj = {
            ...searchObj,
            date: searchObj.date.map((item) =>
              dayjs(item).format("YYYY-MM-DD")
            ),
          };
        else
          searchObj = {
            ...searchObj,
            date: null,
          };

        searchObj = {
          ...searchObj,
          price: searchObj.price
            ? searchObj.price.map((item) => (item ? Number(item) : null))
            : null,
        };
      }

      const res = await getProductList(pagination, sortInfo, searchObj);
      this.pagination = pagination;
      this.tableData = res.list;
      this.totalItmes = res.total;
      this.loading--;
    },
    async handleInsert(data) {
      this.loading++;
      await insertProduct(data);
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
    },
  },
};
</script>

<style>
</style>