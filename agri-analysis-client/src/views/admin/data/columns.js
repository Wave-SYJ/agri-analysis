import { getProvinceList, getMarketList, getCityList, getTypeList, getVarietyList, getVariety, getMarket } from '@/api/category';

function formatFun(item) {
  return {
    title: item.name,
    value: item.id
  };
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
    formatFuns: [formatFun, formatFun],
    degree: 2,
    getOptionsFuns: [
      async () => (await getTypeList()).map((item) => ({ label: item.name, value: item.id, leaf: false })),
      async (typeId) => (await getVarietyList(typeId)).map((item) => ({ label: item.name, value: item.id, leaf: true }))
    ],
    getValuesFun: (item) => [item.type.id, item.id],
    handleChangeFun: async (editingObj, newId) => {
      editingObj.variety_id = newId;
      editingObj.variety = await getVariety(newId);
    }
  },
  {
    title: '价格',
    type: 'number',
    suffix: '元 / 公斤',
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
    formatFuns: [formatFun, formatFun, formatFun],
    degree: 3,
    getOptionsFuns: [
      async () => (await getProvinceList()).map((item) => ({ label: item.name, value: item.id, leaf: false })),
      async (provinceId) => (await getCityList(provinceId)).map((item) => ({ label: item.name, value: item.id, leaf: false })),
      async (cityId) => (await getMarketList(cityId)).map((item) => ({ label: item.name, value: item.id, leaf: true }))
    ],
    getValuesFun: (item) => [item.city.province.id, item.city.id, item.id],
    handleChangeFun: async (editingObj, newId) => {
      editingObj.market_id = newId;
      editingObj.market = await getMarket(newId);
    }
  },
  {
    title: '操作',
    type: 'operations'
  }
];
