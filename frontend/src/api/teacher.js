import request from "@/utils/request";

export function fetchSlogan(query) {
  return request({
    url: "/teacherslogan",
    method: "get",
    params: query,
  });
}

export function fetchList(query) {
  return request({
    url: "/teachers",
    method: "get",
    params: query,
  });
}

export function addTeacher(data) {
  return request({
    url: "/teachers",
    method: "post",
    data,
  });
}

export function updateTeacher(data) {
  return request({
    url: "/teachers/id",
    method: "put",
    data,
  });
}
