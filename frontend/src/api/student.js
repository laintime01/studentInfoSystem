import request from "@/utils/request";

export function fetchSlogan(query) {
  return request({
    url: "/studentslogan",
    method: "get",
    params: query,
  });
}

export function addStudent(data) {
  return request({
    url: "/students",
    method: "post",
    data,
  });
}

export function fetchStudentList(query) {
  return request({
    url: "/students",
    method: "get",
    params: query,
  });
}

export function updateStudent(data, id) {
  return request({
    url: "/students/" + id,
    method: "put",
    data,
  });
}

export function deleteStudent(data, id) {
  return request({
    url: "/students/" + id,
    method: "delete",
    data,
  });
}
