<template>
  <b-jumbotron header="Login" lead="welcome to student information system">
    <div class="container">
      <div>
        <b-alert variant="success" v-if="showMessage" show>
          {{ message }}
        </b-alert>
      </div>
      <b-form @submit="onSubmit">
        <b-form-group
          id="username-group"
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
            type="password"
            placeholder="Enter password"
            v-model="loginForm.password"
            required
            style="width: 60%; margin-top: 20px; display: inline-block"
            >Password</b-form-input
          >
        </b-form-group>
        <b-button type="submit" style="margin-top: 30px">Login</b-button>
        <b-button
          type="register"
          style="margin-top: 30px; margin-left: 30px"
          v-b-modal.register
          >Register</b-button
        >
      </b-form>
      <!-- register modal -->
      <b-modal
        ref="registerModal"
        id="register"
        title="Register"
        hide-backdrop
        hide-footer
      >
        <b-form @submit="onSubmitRegi" @reset="onResetRegi" class="w-100">
          <b-form-group label="Username" label-for="username-input">
            <b-form-input
              id="username-input"
              type="text"
              placeholder="Enter username"
              required
              v-model="registerForm.username"
            >
            </b-form-input>
          </b-form-group>
          <b-form-group label="Password" label-for="passwordname-input">
            <b-form-input
              id="password-input"
              type="password"
              placeholder="Enter password"
              required
              v-model="registerForm.password"
            >
            </b-form-input>
          </b-form-group>
          <b-form-group label="rePassword" label-for="rePassword-input">
            <b-form-input
              id="rePassword-input"
              type="password"
              placeholder="Enter password again"
              required
              v-model="registerForm.rePassword"
              trim
            >
            </b-form-input>
            <!-- This will only be shown if the preceding input has an invalid state -->
            <b-form-invalid-feedback
              id="input-live-feedback"
              v-if="passwordConfirmationRule"
            >
              Password not same
            </b-form-invalid-feedback>
          </b-form-group>
          <b-button type="submit" variant="outline-info">Submit</b-button>
          <b-button
            type="reset"
            variant="outline-danger"
            style="margin-left: 30px"
          >
            Reset
          </b-button>
        </b-form>
      </b-modal>
    </div>
  </b-jumbotron>
</template>

<script>
import { addUser, userLogin } from "@/api/login";
import store from "../store/index";

export default {
  name: "LoginView",
  computed: {
    passwordConfirmationRule() {
      return () => this.password === this.rePassword || "Password must match";
    },
  },
  data() {
    return {
      username: "",
      message: "",
      showMessage: false,
      loginForm: {
        username: "",
        password: "",
      },
      registerForm: {
        username: "",
        password: "",
        rePassword: "",
      },
    };
  },
  methods: {
    loginFunction(data) {
      userLogin(data)
        .then((res) => {
          if (res.status === 201) {
            localStorage.setItem("token", res.data.access_token);
            localStorage.setItem("name", res.data.user);
            store.dispatch("user", res.data.user);
            this.$router.push("/");
          }
        })
        .catch((e) => {
          console.log(e);
          if (e.response) {
            this.message = e.response.statusText;
            this.showMessage = true;
          }
        });
    },
    async onSubmit(event) {
      event.preventDefault();
      const logindata = {
        username: this.loginForm.username,
        password: this.loginForm.password,
      };
      await this.loginFunction(logindata);
    },
    onReset() {
      console.log("reset");
    },
    onSubmitRegi(event) {
      event.preventDefault();
      const payload = {
        username: this.registerForm.username,
        password: this.registerForm.password,
      };
      this.registerUser(payload);
      this.$refs.registerModal.hide();
      alert("registered!");
    },
    onResetRegi() {
      console.log("register reset");
    },
    registerUser(data) {
      addUser(data).then((res) => {
        console.log(res);
      });
    },
  },
};
</script>

<style scoped></style>
