import request from '@/utils/request';
import dayjs from 'dayjs';

export async function getBasicInfo() {
  const { data } = await request({
    url: '/api/monitor/basic',
    method: 'get'
  });
  return data;
}

export async function getCrawls(dateRange, market) {
  let { data } = await request({
    url: '/api/monitor/crawls',
    method: 'post',
    data: {
      dateRange,
      market
    }
  });

  const dates = []
  let current = dayjs(dateRange[0])
  while (current.diff(dateRange[1], 'day') <= 0) {
    dates.push(current)
    current = current.add(1, 'day')
  }

  
  data = data.map(item => JSON.parse(item))
  return dates.map(date => date.format('YYYY-MM-DD')).map(date => ({
    date: date,
    items: data.filter(item => item.date === date)
  }))
}
