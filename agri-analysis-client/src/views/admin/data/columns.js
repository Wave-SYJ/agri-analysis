export default [
  {
    title: '#',
    type: 'index'
  },
  {
    title: '日期',
    type: 'date',
    format: 'YYYY-MM-DD',
    prop: 'date',
    editable: true
  },
  {
    title: '产品',
    type: 'text',
    prop: 'product',
    editable: true
  },
  {
    title: '价格',
    type: 'number',
    suffix: "元 / 公斤",
    prop: 'price',
    editable: true
  },
  {
    title: '市场',
    type: 'text',
    prop: 'market',
    editable: true
  },
  {
    title: '操作',
    type: 'operations'
  }
]