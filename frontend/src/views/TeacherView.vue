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
          <button
            type="button"
            class="btn btn-success"
            style="float: left"
            v-b-modal.teacher-modal
          >
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
              <tr v-for="(teacher, index) in teachers" :key="index">
                <td>{{ teacher.id }}</td>
                <td>{{ teacher.name }}</td>
                <td>{{ teacher.subject }}</td>
                <td>
                  <div class="btn-group" role="group">
                    <button type="button" class="btn btn-info">Update</button>
                    <button type="button" class="btn btn-danger">Delete</button>
                  </div>
                </td>
              </tr>
            </tbody>
          </table>
          <footer class="text-center">
            Copyright &copy;. All Rights Reserved 2022.
          </footer>
        </div>
      </div>
      <!-- First Modal-->
      <b-modal
        ref="addTeacherModal"
        id="teacher-modal"
        title="Add a new teacher"
      >
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
          <b-form-group id="form-id-group" label="ID" label-for="form-id-input">
            <b-form-input
              id="form-id-input"
              type="text"
              v-model="addTeacherForm.id"
              required
              placeholder="Enter Id"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group
            id="form-name-group"
            label="Name"
            label-for="form-name-input"
          >
            <b-form-input
              id="form-name-input"
              type="text"
              v-model="addTeacherForm.name"
              required
              placeholder="Enter Name"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group
            id="form-subject-group"
            label="Subject"
            label-for="form-subject-input"
          >
            <b-form-input
              id="form-subject-input"
              type="text"
              v-model="addTeacherForm.subject"
              required
              placeholder="Enter Subject"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group
            id="form-phone-group"
            label="Phone"
            label-for="form-phone-input"
          >
            <b-form-input
              id="form-phone-input"
              type="text"
              v-model="addTeacherForm.phone"
              required
              placeholder="Enter Name"
            >
            </b-form-input>
          </b-form-group>
          <!--  Buttons: submit and reset-->
          <button type="submit" @click="onSubmit" variant="primary">
            Submit
          </button>
          <button type="reset">Reset</button>
        </b-form>
      </b-modal>
    </div>
  </div>
</template>

<script>
import { fetchSlogan, fetchList, addTeacher } from "@/api/teacher";
export default {
  name: "TeacherView",
  data() {
    return {
      msg: "",
      teachers: "",
      addTeacherForm: {
        id: "",
        name: "",
        subject: "",
        phone: "",
      },
    };
  },
  methods: {
    sloganApi() {
      fetchSlogan().then((res) => {
        console.log(res);
        this.msg = res.data;
      });
    },
    getTeachersList() {
      fetchList()
        .then((res) => {
          console.log(res);
          this.teachers = res.data.teachers;
          console.log(this.teachers);
        })
        .catch((err) => {
          console.log(err);
        });
    },
    addTeacher(payLoad) {
      addTeacher(payLoad)
        .then(() => {
          this.getTeachersList();
        })
        .catch((err) => {
          console.log(err);
        });
    },
    initForm() {
      this.addTeacherForm.id = "";
      this.addTeacherForm.name = "";
      this.addTeacherForm.subject = "";
      this.addTeacherForm.phone = "";
    },
    onSubmit(e) {
      console.log("submitted");
      e.preventDefault();
      this.$refs.addTeacherModal.hide();
      const payLoad = {
        id: this.addTeacherForm.id,
        name: this.addTeacherForm.name,
        subject: this.addTeacherForm.subject,
        phone: this.addTeacherForm.phone,
      };
      this.addTeacher(payLoad);
      this.initForm();
    },
    onReset() {
      console.log("reset");
    },
  },
  created() {
    this.sloganApi();
    this.getTeachersList();
  },
};
</script>

<style scoped></style>
