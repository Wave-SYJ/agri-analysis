export default {
  backgroundColor: '#fff',
  title: {
    text: '农产品价格预测折线图',
    textStyle: {
      color: '#000',
      fontSize: 18,
      fontWeight: 'bold'
    },
    subtext: '已根据您选择的时间段预测价格',
    subtextStyle: {
      color: '#000'
    }
  },
  tooltip: {
    show: true,
    trigger: 'axis',
    axisPointer: {
      type: 'cross',
      crossStyle: {
        color: '#000'
      }
    }
  },
  grid: {
    left: 20,
    right: 20,
    top: 80,
    bottom: 20,
    containLabel: true
  },
  xAxis: {
    show: true,
    axisLabel: {
      interval: 1,
      rotate: -20,
      margin: 30,
      color: '#000',
      align: 'center'
    },
    axisTick: {
      alignWithLabel: true,
      lineStyle: {
        color: '#000'
      }
    },
    data: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
  },
  yAxis: [
    {
      type: 'value',
      name: '￥',
      nameTextStyle: {
        color: '#000'
      },
      axisLabel: {
        color: '#000'
      },
      axisTick: {
        alignWithLabel: true,
        lineStyle: {
          color: '#000'
        }
      },
      splitLine: {
        show: false
      }
    }
  ],
  series: [
    {
      type: 'line',
      name: '测试',
      stack: '人数',
      data: [5, 9, 3, 7, 8, 12, 45, 25, 11, 6, 9, 20],
      label: {
        show: true,
        position: 'insideTop',
        offset: [0, 20],
        color: '#000'
      },
      emphasis: {
        label: {
          color: '#000'
        }
      }
    }
  ]
};
