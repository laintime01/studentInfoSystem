import axios from "axios";

const requests = axios.create({
  baseURL: process.env.VUE_APP_BASE_API || "http://localhost:8900", //url=baseurl+request url
  // withCredentials: true,
  timeout: 5000, // request timeout,
  // headers: {
  //   Authorization: "Bearer " + localStorage.getItem("user").token,
  // },
});

export default requests;
