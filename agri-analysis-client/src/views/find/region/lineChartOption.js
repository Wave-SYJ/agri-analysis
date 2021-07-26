export default {
  title: {
    text: "富士苹果区域行情",
    subtext: "数据来自网络",
  },
  tooltip: {
    trigger: "axis",
    axisPointer: {
      type: "shadow",
    },
  },
  xAxis: {
    type: "value",
  },
  yAxis: {
    type: "category",
    data: [],
  },
  series: [
    {
      data: [],
      type: "bar",
    },
  ],
  grid: {
    left: "25%"
  },
  toolbox: {
    show: true,
    feature: {
      myBackBtn: {
        show: false,
        title: "返回",
        icon: `image://${require("@/assets/images/back.svg")}`,
        onclick: null
      },
    },
  },
}