<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <!-- bootswatch CDN-->
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/lumen/bootstrap.min.css"
        integrity="sha384-GzaBcW6yPIfhF+6VpKMjxbTx6tvR/yRd/yJub90CqoIn2Tz4rRXlSpTFYMKHCifX"
        crossorigin="anonymous"
      />
      <div class="row">
        <div class="col-sm-12">
          <h1>Teacher Information</h1>
          <p>{{ msg }}</p>
          <button type="button" class="btn btn-info" style="float: left">
            Add Info
          </button>
          <br /><br />
          <table class="table table-hover">
            <!--Table Head-->
            <thead>
              <tr>
                <!--Table header cells-->
                <th scope="col">ID</th>
                <th scope="col">Name</th>
                <th scope="col">Subject</th>
                <th scope="col">Phone</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td>10000</td>
                <td>Zheng Hao</td>
                <td>Math</td>
                <td>
                  <div class="btn-group" role="group">
                    <button
                      type="button"
                      class="btn btn-success"
                      style="margin-right: 5px"
                    >
                      Update
                    </button>
                    <button type="button" class="btn btn-danger">Delete</button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>
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
