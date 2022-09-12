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
          <!-- Alert after add teacher -->
          <b-alert variant="success" v-if="showMessage" show
            >{{ message }}
          </b-alert>
          <!--v-b-modal.teacher-modal: bind this button to modal-->
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
                <th scope="col">Act</th>
              </tr>
            </thead>
            <tbody>
              <tr v-for="(teacher, index) in teachers" :key="index">
                <td>{{ teacher.id }}</td>
                <td>{{ teacher.name }}</td>
                <td>{{ teacher.subject }}</td>
                <td>{{ teacher.phone }}</td>
                <td>
                  <div class="btn-group" role="group">
                    <button
                      type="button"
                      class="btn btn-info"
                      v-b-modal.teacher-update-modal
                      @click="editTeacher(teacher)"
                    >
                      Update
                    </button>
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
      <!-- Start First Modal-->
      <!-- hide-backdrop : hide black background and show the original page -->
      <!-- hide-footer: hide the default OK and Cancel button -->
      <b-modal
        ref="addTeacherModal"
        id="teacher-modal"
        title="Add a new teacher"
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
              placeholder="Enter Phone Number"
            >
            </b-form-input>
          </b-form-group>
          <br />
          <!--  Buttons: submit and reset-->
          <b-button type="submit" variant="outline-info">Submit</b-button>
          <b-button type="reset" variant="outline-danger"> Reset </b-button>
        </b-form>
      </b-modal>
      <!--  End of First modal      -->
      <!--      Start of Update Modal-->
      <b-modal
        ref="updateTeacherModal"
        id="teacher-update-modal"
        title="Update a teacher"
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
            id="form-subject-group"
            label="Subject"
            label-for="form-subject-input"
          >
            <b-form-input
              id="form-subject-input"
              type="text"
              v-model="editForm.subject"
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
              v-model="editForm.phone"
              required
              placeholder="Enter Phone Number"
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
  fetchSlogan,
  fetchList,
  addTeacher,
  updateTeacher,
} from "@/api/teacher";
export default {
  name: "TeacherView",
  data() {
    return {
      msg: "",
      teachers: "",
      showMessage: false,
      addTeacherForm: {
        id: "",
        name: "",
        subject: "",
        phone: "",
      },
      editForm: {
        id: "",
        name: "",
        subject: "",
        phone: "",
      },
    };
  },
  message: "",
  methods: {
    sloganApi() {
      fetchSlogan().then((res) => {
        this.msg = res.data;
      });
    },

    getTeachersList() {
      fetchList()
        .then((res) => {
          this.teachers = res.data.teachers;
        })
        .catch((err) => {
          console.log(err);
        });
    },

    addTeacher(payLoad) {
      addTeacher(payLoad)
        .then((res) => {
          this.getTeachersList();
          this.message = res.data.message;
          this.showMessage = true;
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

    onReset(e) {
      // prevent default behavior of the browser
      e.preventDefault();
      this.$refs.addTeacherModal.hide();
      this.initForm();
    },

    editTeacher(teacher) {
      this.editForm = teacher;
    },

    onSubmitUpdate() {
      console.log("on submit update");
    },

    onResetUpdate() {
      console.log("on reset update");
    },

    updateTeacher(payLoad) {
      console.log(payLoad);
      updateTeacher()
        .then((res) => {
          console.log(res);
          this.getTeachersList();
          this.message = "Teacher info Updated!";
          this.showMessage = true;
        })
        .catch((err) => {
          console.log(err);
          this.getTeachersList();
        });
    },
  },

  created() {
    this.sloganApi();
    this.getTeachersList();
  },
};
</script>

<style scoped></style>
