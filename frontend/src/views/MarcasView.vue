<template>
  <div class="marca-container">
    <h2>Listado de Marcas</h2>

    <div v-if="loading" class="info">Cargando marcas...</div>
    <div v-else-if="error" class="error">Ocurrió un error: {{ error.message }}</div>

    <ul v-else class="marca-lista">
      <li v-for="marca in marcas" :key="marca.id">
        {{ marca.nombre }}
      </li>
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

<style scoped>
.marca-container {
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

.marca-lista {
  list-style: none;
  padding: 0;
  margin: 0 auto;
  text-align: left;
}

.marca-lista li {
  padding: 0.5rem 0;
  border-bottom: 1px solid #ddd;
}
</style>
