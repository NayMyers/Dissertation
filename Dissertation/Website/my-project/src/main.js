// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue'
import App from './App'
import Bootstrap from 'bootstrap'
import 'bootstrap/dist/css/bootstrap.min.css'
import router from './router'
import { NavbarPlugin } from 'bootstrap-vue'
// import './styles/style.scss'

Vue.use(NavbarPlugin)

Vue.config.productionTip = false

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  components: { App },
  template: '<App/>'
})
