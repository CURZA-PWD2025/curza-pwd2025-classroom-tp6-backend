import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import MarcasView from '@/views/MarcasView.vue'
import ProveedoresView from '@/views/ProveedoresView.vue'
import ArticulosView  from '@/views/ArticulosView.vue'
import CategoriasView from '@/views/CategoriasView.vue' 



const routes = [
  { path: '/', name: 'home', component: HomeView },
  { path: '/marcas', name: 'marcas', component: MarcasView },
  { path: '/proveedores', name: 'proveedores', component: ProveedoresView },
  { path: '/articulos', name: 'articulos', component: ArticulosView },
  { path: '/categorias', name: 'categorias', component: CategoriasView },
  
]

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export default router
