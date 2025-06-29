import Api from './ApiService'
import type { Categoria } from '@/interfaces/Categorias'
import type { AxiosResponse } from 'axios'

export default {
  getAllCategorias(): Promise<AxiosResponse<Categoria[]>> {
    return Api.getAll('categorias')
  },
  getCategoria(id: number): Promise<AxiosResponse<Categoria>> {
    return Api.getOne('categoria', id)
  },
  createCategoria(data: Categoria): Promise<AxiosResponse<any>> {
    return Api.create('categoria', data)
  },
  updateCategoria(id: number, data: Categoria): Promise<AxiosResponse<any>> {
    return Api.update('categoria', id, data)
  },
  deleteCategoria(id: number): Promise<AxiosResponse<any>> {
    return Api.destroy('categoria', id)
  }
}
