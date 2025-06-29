<template>
  <div class="categoria-container">
    <h2>Listado de Categorías</h2>

    <div v-if="loading" class="info">Cargando categorías...</div>
    <div v-else-if="error" class="error">Ocurrió un error: {{ error.message }}</div>

    <ul v-else class="categoria-lista">
      <li v-for="categoria in categorias" :key="categoria.id">
        {{ categoria.nombre }}
      </li>
    </ul>
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
</script>

<style scoped>
.categoria-container {
  max-width: 600px;
  margin: 2rem auto; /* centra horizontalmente */
  padding: 2rem;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
  text-align: center;
}

h2 {
  margin-bottom: 1rem;
  color: var(--color-primario);
}

.info, .error {
  padding: 1rem;
  border-radius: 6px;
  margin-bottom: 1rem;
}

.info {
  background-color: #e0f0ff;
  color: #0077cc;
}

.error {
  background-color: #ffe0e0;
  color: #cc0000;
}

.categoria-lista {
  list-style: none;
  padding: 0;
  margin: 0 auto;
  text-align: left;
}

.categoria-lista li {
  padding: 0.5rem 0;
  border-bottom: 1px solid #ddd;
}
</style>
