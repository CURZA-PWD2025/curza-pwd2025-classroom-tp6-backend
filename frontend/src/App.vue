<template>
  <div id="app">
    <header class="navbar">
      <h1 class="logo">TP 7</h1>
      <nav class="nav-links">
        <router-link to="/" exact-active-class="active">Inicio</router-link>
        <router-link to="/articulos" exact-active-class="active">Artículos</router-link>
        <router-link to="/marcas" exact-active-class="active">Marcas</router-link>
        <router-link to="/proveedores" exact-active-class="active">Proveedores</router-link>
        <router-link to="/categorias" exact-active-class="active">Categorías</router-link>
      </nav>
    </header>

    <main class="main-content">
      <router-view />
    </main>
  </div>
</template>

<script setup lang="ts">
</script>

<style>

.navbar {
  background-color: var(--color-primario);
  color: #fff;
  padding: 1rem 2rem;
  display: flex;
  justify-content: space-between;
  align-items: center;
}

.logo {
  font-size: 1.5rem;
  font-weight: bold;
  margin: 0;
}

.nav-links {
  display: flex;
  gap: 1rem;
}

.nav-links a {
  color: #fff;
  text-decoration: none;
  font-weight: 500;
  transition: opacity 0.2s ease;
}

.nav-links a:hover {
  opacity: 0.8;
}

.active {
  text-decoration: underline;
}

.main-content {
  padding: 2rem;
  background-color: var(--color-secundario);
  min-height: calc(100vh - 80px);
}
</style>
