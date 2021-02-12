<template>
   <div>
     <!-- <img src="./assets/logo.png"> -->
     <h1>{{ Homepage }}</h1>
       Hello {{ $route.params.name }}
   </div>
</template>
<script>
  export default {
    name: 'firstroute',
    data () {
      return {
      msg: 'FirstRoute'
    }
  }
}
</script>
