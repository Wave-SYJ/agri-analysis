import Cookies from 'js-cookie';
import { getUserInfo as remoteGetUserInfo } from '@/api/admin'

let userInfo = null

export function getToken() {
  return Cookies.get('token');
}

export async function setToken(token) {
  Cookies.set('token', token, { expires: 1 });
}

export function logout() {
  Cookies.remove('token')
  userInfo = null
}

export async function getUserInfo() {
  if (!getToken())
    return null;
  if (userInfo) return userInfo
  userInfo = await remoteGetUserInfo()
  return userInfo
}