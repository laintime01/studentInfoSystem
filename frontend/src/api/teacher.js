import request from "@/utils/request";

export function fetchList(query) {
  return request({
    url: "/teacher",
    method: "get",
    params: query,
  });
}
