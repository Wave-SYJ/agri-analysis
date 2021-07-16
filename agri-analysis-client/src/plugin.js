import Vue from 'vue'
import ElementUI from 'element-ui';
import 'element-ui/lib/theme-chalk/index.css';
import '@/assets/style/global.scss'
import Fragment from 'vue-fragment'
import dayjs from 'dayjs';

Vue.use(ElementUI);
Vue.use(Fragment.Plugin);

dayjs.extend(require('dayjs/plugin/customParseFormat'))