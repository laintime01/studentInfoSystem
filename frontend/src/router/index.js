import Vue from "vue";
import VueRouter from "vue-router";
import HomeView from "../views/HomeView.vue";
import TeacherView from "@/views/TeacherView";
import StudentView from "@/views/StudentView";
import LoginView from "@/views/LoginView";

Vue.use(VueRouter);

const routes = [
  {
    path: "/login",
    name: "login",
    component: LoginView,
    meta: {
      hideNavbar: true,
      auth: false,
    },
  },
  {
    path: "/",
    name: "home",
    component: HomeView,
    meta: {
      auth: true,
    },
  },
  {
    path: "/student",
    name: "student",
    component: StudentView,
    meta: {
      auth: true,
    },
  },
  {
    path: "/teacher",
    name: "teacher",
    component: TeacherView,
    meta: {
      auth: true,
    },
  },
  {
    path: "/about",
    name: "about",
    // route level code-splitting
    // this generates a separate chunk (about.[hash].js) for this route
    // which is lazy-loaded when the route is visited.
    meta: {
      auth: true,
    },
    component: () =>
      import(/* webpackChunkName: "about" */ "../views/AboutView.vue"),
  },
];

const router = new VueRouter({
  mode: "history",
  base: process.env.BASE_URL,
  routes,
});

router.beforeEach((to, from, next) => {
  if (!localStorage.getItem("token")) {
    next("/login");
  } else if (to.path === "/login" && localStorage.getItem("token")) {
    next("/");
  } else {
    next();
  }
});

export default router;
