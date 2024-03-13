import { createRouter, createWebHistory } from 'vue-router';
import App from './App.vue';
import Contattaci from './components/Contattaci.vue';

const routes = [
  {
    path: '/',
    name: 'App',
    component: App
  },
  {
    path: '/Contattaci',
    name: 'Contattaci',
    component: Contattaci
  }
];

const router = createRouter({
  history: createWebHistory(),
  routes
});

export default router;