import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

const state = {
  user: null,
};

export default new Vuex.Store({
  state,
  getters: {
    user: (state) => {
      return state.user;
    },
  },
  mutations: {
    user(state, user) {
      state.user = user;
    },
  },
  actions: {
    user(context, user) {
      context.commit("user", user);
    },
  },
});