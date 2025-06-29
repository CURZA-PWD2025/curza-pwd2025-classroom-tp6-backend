import { defineStore } from 'pinia'
import ProveedorService from '@/services/ProveedorService'
import type { Proveedor } from '@/interfaces/Proveedor'

export const useProveedorStore = defineStore('proveedor', {
  state: () => ({
    proveedores: [] as Proveedor[],
    loading: false,
    error: null as any
  }),
  actions: {
    async fetchProveedores() {
      this.loading = true
      try {
        const res = await ProveedorService.getAllProveedores()
        this.proveedores = res.data
      } catch (err) {
        this.error = err
      } finally {
        this.loading = false
      }
    },
    async deleteProveedor(id: number) {
      await ProveedorService.deleteProveedor(id)
      await this.fetchProveedores()
    }
  }
})
