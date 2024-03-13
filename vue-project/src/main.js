import { createApp } from 'vue';
import App from './App.vue';
import router from './Router.js';

import './assets/main.css'; // Importa il file CSS principale

// Crea l'applicazione Vue e usa il router
const app = createApp(App);
app.use(router);

// Monta l'applicazione Vue sull'elemento con id "app" nel tuo HTML
app.mount('#app');
