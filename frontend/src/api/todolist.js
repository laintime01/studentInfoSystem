import request from "@/utils/request";

export function fetchTodoList(query) {
  return request({
    url: "/todolist",
    method: "get",
    params: query,
  });
}

export function addTodoList(data) {
  return request({
    url: "/todolist",
    method: "post",
    data,
  });
}

export function deleteTodoList(id) {
  return request({
    url: "/todolist/" + id,
    method: "delete",
  });
}
