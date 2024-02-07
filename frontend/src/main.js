import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import PrimeVue from 'primevue/config';

import 'bootstrap/dist/css/bootstrap-grid.min.css'
//import 'bootstrap'
//import 'bootstrap-icons/font/bootstrap-icons.css'

const app = createApp(App)

//import 'primevue/resources/themes/aura-light-green/theme.css'
import "primevue/resources/themes/lara-light-purple/theme.css"
//import "primevue/resources/themes/aura-dark-green/theme.css";
import "primevue/resources/primevue.min.css";
import 'primeicons/primeicons.css'

import "primeflex/primeflex.css";


import Menubar from 'primevue/menubar';
import Button from 'primevue/button';
import Card from 'primevue/card';
import Checkbox from 'primevue/checkbox';


app.use(PrimeVue);
app.use(router)

app.component("Menubar", Menubar);
app.component("Button", Button);
app.component("Card", Card);
app.component("Checkbox", Checkbox);

app.mount('#app')
