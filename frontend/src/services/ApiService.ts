import axios from 'axios'

const apiClient = axios.create({
  baseURL: 'http://localhost:5000', 
  headers: {
    'Content-Type': 'application/json'
  }
})

export default {
  getAll(url:string) {
    return apiClient.get(url)
  },
  getOne(url:string, id:number) {
    return apiClient.get(`${url}/${id}`)
  },
  create(url:string, data:string | object) {
    return apiClient.post(url, data)
  },
  update(url:string, id:number, data:string | object) {
    return apiClient.put(`${url}/${id}`, data)
  },
  destroy(url:string, id:number) {
    return apiClient.delete(`${url}/${id}`)
  }
}
