import Api from './ApiService'
import type { Proveedor } from '@/interfaces/Proveedor'
import type { AxiosResponse } from 'axios'

export default {
  getAllProveedores(): Promise<AxiosResponse<Proveedor[]>> {
    return Api.getAll('proveedores')
  },
  getProveedor(id: number): Promise<AxiosResponse<Proveedor>> {
    return Api.getOne('proveedor', id)
  },
  createProveedor(data: Proveedor): Promise<AxiosResponse<any>> {
    return Api.create('proveedor', data)
  },
  updateProveedor(id: number, data: Proveedor): Promise<AxiosResponse<any>> {
    return Api.update('proveedor', id, data)
  },
  deleteProveedor(id: number): Promise<AxiosResponse<any>> {
    return Api.destroy('proveedor', id)
  }
}
