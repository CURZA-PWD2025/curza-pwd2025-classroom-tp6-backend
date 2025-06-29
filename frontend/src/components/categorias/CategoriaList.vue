<template>
  <div class="categoria-container">
    <h2>Listado de Categorías</h2>

    <div v-if="loading" class="info">Cargando categorías...</div>
    <div v-else-if="error" class="error">Ocurrió un error: {{ error.message }}</div>

    <div v-else class="card-grid">
      <div class="categoria-card" v-for="categoria in categorias" :key="categoria.id">
        <p class="categoria-nombre">{{ categoria.nombre }}</p>
        <button @click="eliminar(categoria.id!)">Eliminar</button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { useCategoriaStore } from '@/stores/categoriaStore'

const categoriaStore = useCategoriaStore()
const { categorias, loading, error } = categoriaStore

onMounted(() => {
  categoriaStore.fetchCategorias()
})

function eliminar(id: number) {
  if (confirm('¿Eliminar esta categoría?')) {
    categoriaStore.deleteCategoria(id)
  }
}
</script>

<style scoped>
.categoria-container {
  padding: 2rem;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}

.categoria-card {
  background-color: var(--color-secundario);
  padding: 1rem;
  border-radius: 6px;
  display: flex;
  justify-content: space-between;
  align-items: center;
  transition: box-shadow 0.2s ease;
}

.categoria-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.categoria-nombre {
  font-weight: 600;
}
</style>
