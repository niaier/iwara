import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/antd.css';

import axios from 'axios';
// axios.defaults.baseURL='http://localhost:8080/api'
axios.defaults.baseURL='http://192.168.50.221:8080/api'


// import axios from 'axios';
// import VueAxios from 'vue-axios';
Vue.use(Antd);
// Vue.prototype.$axios = axios;
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
