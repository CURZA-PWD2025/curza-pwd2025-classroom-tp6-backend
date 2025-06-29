import Api from './ApiService'
import type { Articulo } from '@/interfaces/Articulo'
import type { AxiosResponse } from 'axios'

export default {
  getAllArticulos(): Promise<AxiosResponse<Articulo[]>> {
    return Api.getAll('articulos')
  },
  getArticulo(id: number): Promise<AxiosResponse<Articulo>> {
    return Api.getOne('articulo', id)
  },
  createArticulo(data: Articulo): Promise<AxiosResponse<any>> {
    return Api.create('articulo', data)
  },
  updateArticulo(id: number, data: Articulo): Promise<AxiosResponse<any>> {
    return Api.update('articulo', id, data)
  },
  deleteArticulo(id: number): Promise<AxiosResponse<any>> {
    return Api.destroy('articulo', id)
  }
}
