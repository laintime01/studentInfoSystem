<template>
  <div>
    <h1>Teacher View</h1>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "TeacherView",
  data() {
    return {
      msg: "Hello, this is teacher page!",
    };
  },
  methods: {
    getRes() {
      const path = "http://localhost:8900/teacher";
      axios.get(path).then((res) => {
        console.log(res.data);
        this.msg = res.data;
      });
    },
  },
  created() {
    this.getRes();
  },
};
</script>

<style scoped></style>
