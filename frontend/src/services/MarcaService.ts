import Api from './ApiService'
import type { Marca } from '@/interfaces/Marca'
import type { AxiosResponse } from 'axios'

export default {
  getAllMarcas(): Promise<AxiosResponse<Marca[]>> {
    return Api.getAll('marcas')
  },
  getMarca(id: number): Promise<AxiosResponse<Marca>> {
    return Api.getOne('marca', id)
  },
  createMarca(data: Marca): Promise<AxiosResponse<any>> {
    return Api.create('marca', data)
  },
  updateMarca(id: number, data: Marca): Promise<AxiosResponse<any>> {
    return Api.update('marca', id, data)
  },
  deleteMarca(id: number): Promise<AxiosResponse<any>> {
    return Api.destroy('marca', id)
  }
}
