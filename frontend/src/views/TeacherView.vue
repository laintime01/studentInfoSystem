<template>
  <div>
    <h1>Teacher View</h1>
    <p>{{ msg }}</p>
  </div>
</template>

<script>
import { fetchList } from "@/api/teacher";
export default {
  name: "TeacherView",
  data() {
    return {
      msg: "",
    };
  },
  methods: {
    teacherApi() {
      fetchList().then((res) => {
        console.log(res);
        this.msg = res.data;
      });
    },
  },
  created() {
    this.teacherApi();
  },
};
</script>

<style scoped></style>
