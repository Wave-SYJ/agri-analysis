import request from '@/utils/request';

export async function getBasicInfo() {
  const { data } = await request({
    url: '/api/monitor/basic',
    method: 'get'
  });
  return data
}
