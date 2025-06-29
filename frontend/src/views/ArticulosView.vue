<template>
  <div class="articulo-container">
    <h2>Listado de Artículos</h2>

    <div v-if="loading" class="info">Cargando artículos...</div>
    <div v-else-if="error" class="error">Ocurrió un error: {{ error.message }}</div>

    <div v-else class="card-grid">
      <div class="articulo-card" v-for="articulo in articulos" :key="articulo.id">
  <div class="contenido">
    <p class="titulo">{{ articulo.marca.nombre }}</p>
    <p>Precio: ${{ articulo.precio }}</p>
    <p>Stock: {{ articulo.stock }}</p>
  </div>
  <button @click="eliminar(articulo.id!)">Eliminar</button>
</div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { useArticuloStore } from '@/stores/articuloStore'

const articuloStore = useArticuloStore()
const { articulos, loading, error } = articuloStore

onMounted(() => {
  articuloStore.fetchArticulos()
})

function eliminar(id: number) {
  if (confirm('¿Eliminar este artículo?')) {
    articuloStore.deleteArticulo(id)
  }
}
</script>

<style scoped>
.articulo-container {
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

.articulo-card {
  background-color: var(--color-secundario);
  padding: 1rem;
  border-radius: 6px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.2s ease;
}

.articulo-card:hover {
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
}

.titulo {
  font-weight: bold;
  margin-bottom: 0.5rem;
}

button {
  margin-top: 1rem;
}
</style>
