import { defineStore } from 'pinia'
import MarcaService from '@/services/MarcaService'
import type { Marca } from '@/interfaces/Marca'

export const useMarcaStore = defineStore('marca', {
  state: () => ({
    marcas: [] as Marca[],
    loading: false,
    error: null as any
  }),
  actions: {
    async fetchMarcas() {
      this.loading = true
      try {
        const res = await MarcaService.getAllMarcas()
        this.marcas = res.data
      } catch (err) {
        this.error = err
      } finally {
        this.loading = false
      }
    },
    async deleteMarca(id: number) {
      await MarcaService.deleteMarca(id)
      await this.fetchMarcas()
    }
  }
})
