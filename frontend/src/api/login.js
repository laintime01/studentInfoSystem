import request from "@/utils/request";

export function addUser(data) {
  return request({
    url: "/register",
    method: "post",
    data,
  });
}

export function userLogin(data) {
  return request({
    url: "/login",
    method: "post",
    data,
  });
}
