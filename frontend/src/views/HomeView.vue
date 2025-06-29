<template>
  <div class="home-container">
    <h1>Trabajo Práctico N° 7</h1>
    <div class="botonera">
      <router-link to="/articulos" class="btn-nav">Artículos</router-link>
      <router-link to="/marcas" class="btn-nav">Marcas</router-link>
      <router-link to="/proveedores" class="btn-nav">Proveedores</router-link>
      <router-link to="/categorias" class="btn-nav">Categorías</router-link>
    </div>
  </div>
</template>

<script setup lang="ts">

</script>

<style scoped>
.home-container {
  text-align: center;
  padding: 3rem;
  background-color: var(--color-secundario);
}

h1 {
  margin-bottom: 2rem;
  color: var(--color-primario);
}

.botonera {
  display: flex;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
}

.btn-nav {
  background-color: var(--color-boton);
  color: #fff;
  text-decoration: none;
  padding: 0.75rem 1.5rem;
  border-radius: 8px;
  font-weight: 600;
  transition: background-color 0.2s ease;
}

.btn-nav:hover {
  background-color: var(--color-boton-hover);
}
</style>
