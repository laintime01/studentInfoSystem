<template>
  <div id="app">
    <nav v-if="!$route.meta.hideNavbar">
      <router-link to="/">Home</router-link> |
      <router-link to="/student">Student</router-link> |
      <router-link to="/teacher">Teacher</router-link> |
      <router-link to="/about">About</router-link>
      <b-button
        variant="outline-primary"
        style="float: right"
        v-on:click="this.logout"
        v-show="isLogin"
        >logout</b-button
      >
    </nav>
    <router-view />
  </div>
</template>

<script>
export default {
  data() {
    return {
      isLogin: false,
    };
  },
  methods: {
    logout() {
      localStorage.removeItem("token");
      localStorage.removeItem("name");
      this.$router.push("/login");
    },
    getLoginStatus() {
      this.isLogin = !!localStorage.getItem("token");
    },
  },
  created() {
    this.getLoginStatus();
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
}

nav a {
  font-weight: bold;
  color: #2c3e50;
}

nav a.router-link-exact-active {
  color: #42b983;
}
</style>
