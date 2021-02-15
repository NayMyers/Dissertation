<template>
   <div>
     <!-- <img src="./assets/logo.png"> -->
     <h1>{{ Homepage }}</h1>
       Hello {{ $route.params.name }}
      <input type="file" name="fileInput" value="Select File" @change="onFileSelected">
      <button @click="onUpload" type="button" name="button">Upload</button>
      <button @click="testAPIRes" type="button" name="button">Test API res</button>

   </div>

</template>
<script>
  const axios = require('Axios');
  export default {
    name: 'firstroute',
    data () {
      return {
      selectedFile: null
    }
  },
  methods: {
    onFileSelected(event){
      this.selectedFile = event.target.files[0]
    },
    onUpload(){
      const fd = new FormData();
      fd.append('image', this.selectedFile, this.selectedFile.name)
      axios.post('http://127.0.0.1:5000/upload_image')
        .then(res =>{
          console.log(res)
        })
    },
    testAPIRes(){

      axios.post('http://127.0.0.1:5000/upload_image/helloworld')
            .then(res =>{
              console.log(res)
              /*
               TODO:// Work out how to get rid of the  XMLHttpRequest at
               'http://127.0.0.1:5000/upload_image/helloworld' from origin
               'http://localhost:8080' has been blocked by CORS policy: No
              'Access-Control-Allow-Origin' header is present on the requested
              resource.
              */
            })
    }
  }
}
</script>
