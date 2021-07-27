import axios from 'axios';
import { getToken } from '@/utils/auth';

const request = axios.create();
request.interceptors.request.use(
  (config) => {
    const token = getToken();
    if (token) config.headers['X-Token'] = token;
    return config
  },
  (error) => {
    throw error
  }
);

export default request;
