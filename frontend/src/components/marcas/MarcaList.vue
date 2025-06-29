<template>
  <div>
    <h2>Marcas</h2>
    <div v-if="loading">Cargando...</div>
    <div v-else-if="error">Error: {{ error.message }}</div>
    <ul v-else>
      <li v-for="marca in marcas" :key="marca.id">{{ marca.nombre }}</li>
    </ul>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { useMarcaStore } from '@/stores/marcaStore'

const marcaStore = useMarcaStore()
const { marcas, loading, error } = marcaStore

onMounted(() => {
  marcaStore.fetchMarcas()
})
</script>
