import { defineStore } from 'pinia'
import ArticuloService from '@/services/ArticuloService'
import type { Articulo } from '@/interfaces/Articulo'

export const useArticuloStore = defineStore('articulo', {
  state: () => ({
    articulos: [] as Articulo[],
    loading: false,
    error: null as any
  }),
  actions: {
    async fetchArticulos() {
      this.loading = true
      try {
        const res = await ArticuloService.getAllArticulos()
        this.articulos = res.data
      } catch (err) {
        this.error = err
      } finally {
        this.loading = false
      }
    },
    async deleteArticulo(id: number) {
      await ArticuloService.deleteArticulo(id)
      await this.fetchArticulos()
    }
  }
})
