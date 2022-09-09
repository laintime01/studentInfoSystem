// post-packaging axios
import axios from "vue-axios";

axios.defaults.withCredentials = true

// create instance
const requests = axios.create({
    baseURL: process.env.VUE_APP_BASEURL || 'http://localhost:8080',
    // request time 5s
    timeput: 5000,
})

export default requests