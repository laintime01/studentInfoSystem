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

export function addTeacher(params) {
  return request({
    url: "/teachers",
    method: "post",
    params,
  });
}
