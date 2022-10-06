import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import "bootstrap/dist/css/bootstrap.css"; //install bootstrap first
import BootstrapVue from "bootstrap-vue";
import store from "./store/index";
Vue.config.productionTip = false;
Vue.use(BootstrapVue);

router.beforeEach((to, from, next) => {
  if (localStorage.getItem("token")) {
    next();
    console.log("next!");
  }
});

new Vue({
  router,
  store,
  render: (h) => h(App),
}).$mount("#app");
