import Vue from 'vue'
import App from './App.vue'
import router from './router'
import store from './store'
import Antd from 'ant-design-vue';
import 'ant-design-vue/dist/antd.css';



// import axios from 'axios';
// import VueAxios from 'vue-axios';

Vue.use(Antd);

// Vue.prototype.$axios = axios;

// axios.defaults.baseURL='http://127.0.0.1:3000';
Vue.config.productionTip = false;

new Vue({
  router,
  store,
  render: h => h(App)
}).$mount('#app')
