import request from '@/utils/request';

export async function getAdminList() {
  const { data } = await request({
    method: 'get',
    url: '/api/admin/'
  });
  return data;
}

export async function insertAdmin(data) {
  await request({
    method: 'put',
    url: '/api/admin/',
    data
  })
}

export async function deleteAdmins(list) {
  await request({
    method: 'delete',
    url: '/api/admin/',
    data: list
  })
}
