<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>
      This is a Full-Stack project to create a Student information system using
      VueJs for frontend UI and Flask for the backend server and Flask Rest API
      to connect to the frontend,<br />
      check out the
      <a href="https://www.haoo.tech" target="_blank" rel="noopener"
        >Hao's Page</a
      >.
    </p>
    <p>welcome back, {{ userinfo }}</p>
    <div class="jumbotron vertical-center">
      <div class="container">
        <link
          rel="stylesheet"
          href="https://cdn.jsdelivr.net/npm/bootswatch@4.5.2/dist/sketchy/bootstrap.min.css"
          integrity="sha384-RxqHG2ilm4r6aFRpGmBbGTjsqwfqHOKy1ArsMhHusnRO47jcGqpIQqlQK/kmGy9R"
          crossorigin="anonymous"
        />
        <div class="row">
          <div class="col-sm-12">
            <h3>School schedule</h3>
            <p>Daily schedule of school</p>
            <br />
            <!--headline-->
            <div style="background-color: #2f2f2f">
              <h4
                style="
                  color: #eeeeee;
                  margin-left: -10%;
                  display: inline-block;
                  margin-right: 200px;
                "
              >
                ToDoList
              </h4>
              <b-form-input
                v-model="todo_text"
                style="display: inline-block; width: 30%"
              ></b-form-input>
              <b-button
                style="display: inline-block; background-color: #999999"
                v-on:click="this.onAdd"
                >Add</b-button
              >
            </div>
            <div style="margin-top: 30px">
              <h4 style="float: left">OnGoing</h4>
              <br />
            </div>
            <div style="margin-top: 30px">
              <table class="table table-hover">
                <thead>
                  <tr>
                    <th scope="col">Task</th>
                    <th scope="col">Act</th>
                  </tr>
                </thead>
                <tbody>
                  <tr v-for="(task, index) in todolists" :key="index">
                    <td>{{ task }}</td>
                    <td>
                      <div class="btn-group" role="group">
                        <button
                          type="button"
                          class="btn btn-danger"
                          @click="onDeleteTask(index)"
                        >
                          Done
                        </button>
                      </div>
                    </td>
                  </tr>
                </tbody>
              </table>
            </div>
          </div>
        </div>
      </div>
    </div>
    <footer class="text-center">
      Copyright &copy;. All Rights Reserved 2022.
    </footer>
  </div>
</template>

<script>
import { addTodoList, deleteTodoList, fetchTodoList } from "@/api/todolist";
import { mapGetters } from "vuex";

export default {
  name: "MainPage",
  data() {
    return {
      todo_text: "",
      userinfo: "",
      todolists: "",
      registerForm: {
        username: "",
        password: "",
        password2: "",
      },
    };
  },
  props: {
    msg: String,
  },
  methods: {
    onAdd() {
      const payload = {
        task: this.todo_text,
      };
      console.log(payload);
      this.addList(payload);
    },
    addList(payload) {
      addTodoList(payload).then(() => {
        this.fetchTodoListFunc();
      });
    },
    fetchTodoListFunc() {
      fetchTodoList().then((res) => {
        this.todolists = res.data.todolist;
      });
    },
    getUsername() {
      const current_user = localStorage.getItem("name");
      this.userinfo = current_user;
      console.log(current_user);
    },
    delete_task(id) {
      deleteTodoList(id).then((res) => {
        this.fetchTodoListFunc();
        this.message = res.data.message;
      });
    },
    onDeleteTask(index) {
      console.log(index);
      this.delete_task(index);
    },
  },
  computed: {
    ...mapGetters(["user"]),
  },
  created() {
    this.fetchTodoListFunc();
    this.getUsername();
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h3 {
  margin: 40px 0 0;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
</style>
