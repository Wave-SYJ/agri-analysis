<template>
  <DataTable :tableData="tableData" :columns="columns" />
</template>

<script>
import DataTable from "@/components/DataTable"
import tableData from './fakeData'
import columns from './columns'

import { getProductList } from "@/api/product"

export default {
  components: {
    DataTable
  },
  data() {
    return {
      tableData,
      columns
    }
  },
  async created() {
    console.log(await getProductList())
  }
}
</script>

<style>

</style>