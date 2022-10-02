<template>
  <b-jumbotron header="Login" lead="welcome to student information system">
    <div class="container">
      <b-form @submit="onSubmit">
        <b-form-group
          id="username"
          label-for="input-username"
          style="margin-top: 30px"
        >
          <b-form-input
            id="input-username"
            placeholder="Enter username"
            v-model="loginForm.username"
            style="width: 60%; margin-top: 30px; display: inline-block"
            required
            >Username</b-form-input
          >
        </b-form-group>
        <b-form-group style="margin-top: 20px">
          <b-form-input
            id="input-password"
            placeholder="Enter password"
            v-model="loginForm.password"
            required
            style="width: 60%; margin-top: 20px; display: inline-block"
            >Password</b-form-input
          >
        </b-form-group>
        <b-button type="submit" style="margin-top: 30px">Login</b-button>
      </b-form>
    </div>
  </b-jumbotron>
</template>

<script>
export default {
  name: "LoginView",
  data() {
    return {
      loginForm: {
        username: "",
        password: "",
      },
    };
  },
  methods: {
    onSubmit(event) {
      event.preventDefault();
      alert(JSON.stringify(this.loginForm));
    },
  },
};
</script>

<style scoped></style>
