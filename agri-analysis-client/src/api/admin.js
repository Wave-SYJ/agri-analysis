import request from '@/utils/request';

export async function getAdminList(pagination, sortInfo, searchObj) {
  const { data } = await request({
    method: 'post',
    url: `/api/admin`,
    data: {
      pagination,
      sortInfo,
      searchObj
    }
  });
  return data;
}

export async function insertAdmin(data) {
  await request({
    method: 'put',
    url: '/api/admin',
    data
  })
}

export async function deleteAdmins(list) {
  await request({
    method: 'delete',
    url: '/api/admin',
    data: list
  })
}

export async function updateAdmin(data) {
  await request({
    method: 'patch',
    url: '/api/admin',
    data
  })
}