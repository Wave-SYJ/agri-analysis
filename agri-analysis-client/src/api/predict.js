import request from '@/utils/request';

export async function getPredictData(dateRange, marketId, varietyId) {
  const { data } = await request({
    url: '/api/predict',
    data: {
      dateRange,
      marketId,
      varietyId
    },
    method: 'post'
  });

  return data;
}
