<template>
  <DataTable :tableData="tableData" :columns="columns" />
</template>

<script>
import DataTable from "@/components/DataTable"
import tableData from './fakeData'
import columns from './columns'

export default {
  components: {
    DataTable
  },
  data() {
    return {
      tableData,
      columns
    }
  }
}
</script>

<style>

</style>