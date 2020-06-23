import Vue from 'vue';
import App from './App.vue';
import store from './store';
import { BootstrapVue} from 'bootstrap-vue';
Vue.config.productionTip = false;
// Load BootstrapVue
Vue.use(BootstrapVue);

new Vue({
  store,
  render: h => h(App)
}).$mount('#app');
