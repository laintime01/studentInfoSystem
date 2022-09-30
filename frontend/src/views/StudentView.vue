<template>
  <div class="jumbotron vertical-center">
    <div class="container">
      <link
        rel="stylesheet"
        href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/lumen/bootstrap.min.css"
        integrity="sha384-GzaBcW6yPIfhF+6VpKMjxbTx6tvR/yRd/yJub90CqoIn2Tz4rRXlSpTFYMKHCifX"
        crossorigin="anonymous"
      />
      <div class="row">
        <div class="col-sm-12">
          <h1>Student Information</h1>
          <p>{{ msg }}</p>
          <!--Notice after add student-->
          <b-alert variant="success" v-if="showMessage" show>
            {{ message }}
          </b-alert>
          <button
            type="button"
            class="btn btn-success"
            style="float: left"
            v-b-modal.student-modal
          >
            Add Student
          </button>
          <br /><br />
          <table class="table table-hover">
            <thead>
              <tr>
                <th scope="col">ID</th>
                <th scope="col">NAME</th>
                <th scope="col">SEX</th>
                <th scope="col">AGE</th>
                <th scope="col">FACULTY</th>
                <th scope="col">ACT</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(student, index) in students" :key="index">
                <td>{{ student.id }}</td>
                <td>{{ student.name }}</td>
                <td>{{ student.sex }}</td>
                <td>{{ student.age }}</td>
                <td>{{ student.faculty }}</td>
                <td>
                  <div class="btn-group" role="group">
                    <button
                      type="button"
                      class="btn btn-info"
                      v-b-modal.student-update-modal
                      @click="editStudent(student)"
                    >
                      Update
                    </button>
                    <button
                      type="button"
                      class="btn btn-danger"
                      @click="onDeleteStudent(student)"
                    >
                      Delete
                    </button>
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
      <!--add student modal-->
      <b-modal
        ref="addStudentModal"
        id="student-modal"
        title="Add a new student"
        hide-backdrop
        hide-footer
      >
        <b-form @submit="onSubmit" @reset="onReset" class="w-100">
          <b-form-group
            id="form-name-group"
            label="Name"
            label-for="form-name-input"
          >
            <b-form-input
              id="form-name-input"
              type="text"
              v-model="addStudentForm.name"
              required
              placeholder="Enter Name"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group
            id="form-sex-group"
            label="Sex"
            label-for="form-sex-select"
          >
            <b-form-select
              id="form-sex-select"
              type="text"
              v-model="addStudentForm.sex"
            >
              <option :value="null" disabled>Please select gender</option>
              <option value="Male" selected="selected">Male</option>
              <option value="Female">Female</option>
            </b-form-select>
          </b-form-group>

          <b-form-group
            id="form-age-group"
            label="Age"
            label-for="form-age-input"
          >
            <b-form-input
              id="form-age-input"
              type="text"
              v-model="addStudentForm.age"
              required
              placeholder="Enter Age"
            >
            </b-form-input>
          </b-form-group>
          <b-form-group
            id="form-faculty-group"
            label="Faculty"
            label-for="form-faculty-input"
          >
            <b-form-input
              id="form-faculty-input"
              type="text"
              v-model="addStudentForm.faculty"
              required
              placeholder="Enter Faculty"
            >
            </b-form-input>
          </b-form-group>
          <br />
          <!--  Buttons: submit and reset-->
          <b-button type="submit" variant="outline-info">Submit</b-button>
          <b-button type="reset" variant="outline-danger"> Reset </b-button>
        </b-form>
      </b-modal>
      <!--end of add modal-->
      <!--start of update modal-->
      <b-modal
        ref="updateStudentModal"
        id="student-update-modal"
        title="Update a student"
        hide-backdrop
        hide-footer
      >
        <b-form @submit="onSubmitUpdate" @reset="onResetUpdate" class="w-100">
          <b-form-group
            id="form-name-group"
            label="Name"
            label-for="form-name-input"
          >
            <b-form-input
              id="form-name-input"
              type="text"
              v-model="editForm.name"
              required
              placeholder="Enter Name"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group
            id="form-sex-group"
            label="Sex"
            label-for="form-sex-dropdown"
          >
            <b-form-select
              id="form-sex-dropdown"
              v-model="editForm.sex"
              text="Select Sex"
            >
              <option value="Male">Male</option>
              <option value="Female">Female</option>
            </b-form-select>
          </b-form-group>

          <b-form-group
            id="form-age-group"
            label="Age"
            label-for="form-age-input"
          >
            <b-form-input
              id="form-age-input"
              type="text"
              v-model="editForm.age"
              required
              placeholder="Enter Age"
            >
            </b-form-input>
          </b-form-group>

          <b-form-group
            id="form-faculty-group"
            label="Faculty"
            label-for="form-faculty-input"
          >
            <b-form-input
              id="form-faculty-input"
              type="text"
              v-model="editForm.faculty"
              required
              placeholder="Enter Faculty"
            >
            </b-form-input>
          </b-form-group>
          <br />
          <!--  Buttons: submit and reset-->
          <b-button type="submit" variant="outline-info">Submit</b-button>
          <b-button type="reset" variant="outline-danger"> Reset </b-button>
        </b-form>
      </b-modal>
      <!--      End of Update Modal-->
    </div>
  </div>
</template>

<script>
import {
  addStudent,
  deleteStudent,
  fetchSlogan,
  fetchStudentList,
  updateStudent,
} from "@/api/student";

export default {
  name: "StudentView",
  data() {
    return {
      msg: "",
      students: "",
      showMessage: false,
      message: "",
      addStudentForm: {
        id: "",
        name: "",
        sex: "null",
        age: "",
        faculty: "",
      },
      editForm: {
        id: "",
        name: "",
        sex: "",
        age: "",
        faculty: "",
      },
    };
  },
  methods: {
    editStudent(student) {
      this.editForm = student;
    },
    onDeleteStudent(student) {
      this.delStudentFunc(student, student.id);
    },
    initStudentForm() {
      this.addStudentForm.name = "";
      this.addStudentForm.sex = "";
      this.addStudentForm.age = "";
      this.addStudentForm.faculty = "";
      this.editForm.name = "";
      this.editForm.sex = "";
      this.editForm.age = "";
      this.editForm.faculty = "";
    },
    getSlogan() {
      fetchSlogan().then((res) => {
        this.msg = res.data;
      });
    },
    fetchStudents() {
      fetchStudentList()
        .then((res) => {
          this.students = res.data.students;
        })
        .catch((error) => {
          console.log(error);
        });
    },
    addStudentFunc(payload) {
      addStudent(payload).then((res) => {
        this.fetchStudents();
        this.message = res.data.message;
        this.showMessage = true;
      });
    },
    onSubmit(e) {
      e.preventDefault();
      this.$refs.addStudentModal.hide();
      const payload = {
        name: this.addStudentForm.name,
        sex: this.addStudentForm.sex,
        age: this.addStudentForm.age,
        faculty: this.addStudentForm.faculty,
      };
      this.addStudentFunc(payload);
      this.initStudentForm();
    },
    onReset() {
      this.initStudentForm();
    },
    delStudentFunc(payload, id) {
      deleteStudent(payload, id).then((res) => {
        this.fetchStudents();
        this.message = res.data.message;
        this.showMessage = true;
      });
    },
    updateStudentFunc(payLoad, id) {
      updateStudent(payLoad, id).then(() => {
        this.fetchStudents();
        this.message = "student information updated!";
        this.showMessage = true;
      });
    },
    onSubmitUpdate(e) {
      e.preventDefault();
      this.$refs.updateStudentModal.hide();
      const payload = {
        name: this.editForm.name,
        sex: this.editForm.sex,
        age: this.editForm.age,
        faculty: this.editForm.faculty,
      };
      this.updateStudentFunc(payload, this.editForm.id);
    },
    onResetUpdate() {
      this.initStudentForm();
    },
  },
  created() {
    this.getSlogan();
    this.fetchStudents();
  },
};
</script>

<style scoped></style>
