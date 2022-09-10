<template>
  <div class="home">
    <MainPage msg="Welcome to Our Student Information System" />
  </div>
</template>

<script>
// @ is an alias to /src
import MainPage from "@/components/MainPage.vue";

export default {
  name: "HomeView",
  components: {
    MainPage,
  },
};
</script>
