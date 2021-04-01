import Vue from 'vue'
import Router from 'vue-router'
import HelloWorld from '@/components/HelloWorld'
import Upload_Image from '@/components/Upload_Image'
import Axios from 'axios';


Vue.use(Router)
const axios = require('axios');


export default new Router({
  routes: [
    {
      path: '/HelloWorld',
      name: 'HelloWorld',
      component: HelloWorld
    },
    {
      path: '/Upload_Image',
      name:'Upload_Image',
      component: Upload_Image
    }
  ]
})
