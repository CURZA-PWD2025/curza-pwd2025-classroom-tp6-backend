import { defineStore } from 'pinia'
import CategoriaService from '@/services/CategoriaService'
import type { Categoria } from '@/interfaces/Categorias'

export const useCategoriaStore = defineStore('categoria', {
  state: () => ({
    categorias: [] as Categoria[],
    loading: false,
    error: null as any
  }),
  actions: {
    async fetchCategorias() {
      this.loading = true
      try {
        const res = await CategoriaService.getAllCategorias()
        this.categorias = res.data
      } catch (err) {
        this.error = err
      } finally {
        this.loading = false
      }
    },
    async deleteCategoria(id: number) {
      await CategoriaService.deleteCategoria(id)
      await this.fetchCategorias()
    }
  }
})
