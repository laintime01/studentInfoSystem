import request from "@/utils/request";

export function addUser(data) {
  return request({
    url: "/register",
    method: "post",
    data,
  });
}
