import axios from 'axios'

const api = axios.create({
  baseURL: import.meta.env.VITE_APP_API_BASEURL,
  timeout: 60000,
  responseType: 'json'
})

api.interceptors.response.use(
  response => {
      return Promise.resolve(response.data)
  },
)

export function getRequest(config: any) {
  return api.request({ ...config, method: 'GET' })
}

export function postRequest(config: any) {
  return api.request({ ...config, method: 'POST' })
}

export default api
