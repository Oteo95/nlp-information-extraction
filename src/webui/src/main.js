import Vue from 'vue'
import store from './store'
import App from './App.vue'
import router from './router'
import vuetify from './plugins/vuetify'
import shortkey from '@/plugins/vue-shortkey'
import apollo from './js/apolloClient'

Vue.config.productionTip = false
Vue.prototype.$apollo = apollo

let app 
if(!app){
  new Vue({
    router,
    store,
    vuetify,
    shortkey,
    render: h => h(App)
  }).$mount('#app')
}
