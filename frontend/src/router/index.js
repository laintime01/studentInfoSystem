import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import TeacherView from "@/views/TeacherView";
import StudentView from "@/views/StudentView";
import LoginView from "@/views/LoginView";

Vue.use(VueRouter);

const routes = [
  {
    path: "/",
    name: "login",
    component: LoginView,
    meta: {
      hideNavbar: true,
    },
  },
  {
    path: "/home",
    name: "home",
    component: HomeView,
  },
  {
    path: "/student",
    name: "student",
    component: StudentView,
  },
  {
    path: "/teacher",
    name: "teacher",
    component: TeacherView,
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

export default router;
