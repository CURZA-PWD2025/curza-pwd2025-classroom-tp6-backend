<template>
  <div class="proveedor-container">
    <h2>Listado de Proveedores</h2>

    <div v-if="loading" class="info">Cargando proveedores...</div>
    <div v-else-if="error" class="error">Ocurrió un error: {{ error.message }}</div>

    <div v-else class="card-grid">
      <div class="proveedor-card" v-for="proveedor in proveedores" :key="proveedor.id">
        <div class="contenido">
          <p class="titulo">{{ proveedor.nombre }}</p>
          <p v-if="proveedor.email">📧 {{ proveedor.email }}</p>
          <p v-if="proveedor.telefono">📞 {{ proveedor.telefono }}</p>
        </div>
        <button @click="eliminar(proveedor.id!)">Eliminar</button>
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import { onMounted } from 'vue'
import { useProveedorStore } from '@/stores/proveedorStore'

const proveedorStore = useProveedorStore()
const { proveedores, loading, error } = proveedorStore

onMounted(() => {
  proveedorStore.fetchProveedores()
})

function eliminar(id: number) {
  if (confirm('¿Eliminar este proveedor?')) {
    proveedorStore.deleteProveedor(id)
  }
}
</script>

<style scoped>
.proveedor-container {
  padding: 2rem;
  background-color: #fff;
  border-radius: 8px;
  box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(260px, 1fr));
  gap: 1rem;
  margin-top: 1rem;
}

.proveedor-card {
  background-color: var(--color-secundario);
  padding: 1rem;
  border-radius: 6px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
  box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
  transition: box-shadow 0.2s ease;
}

.proveedor-card:hover {
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
