function formatFun(item) {
  return {
    title: item.name,
    value: item.id
  }
}

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
    editable: true,
    searchable: true
  },
  {
    title: '品种',
    type: 'cascade',
    prop: 'variety',
    editable: true,
    searchable: true,
    formatFuns: [formatFun, formatFun]
  },
  {
    title: '价格',
    type: 'number',
    suffix: "元 / 公斤",
    prop: 'price',
    editable: true,
    searchable: true,
    precision: 2,
    step: 0.1
  },
  {
    title: '市场',
    type: 'cascade',
    prop: 'market',
    editable: true,
    searchable: true,
    formatFuns: [formatFun, formatFun, formatFun]
  },
  {
    title: '操作',
    type: 'operations'
  }
]