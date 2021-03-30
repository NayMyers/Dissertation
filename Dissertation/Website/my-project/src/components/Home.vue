<template>
   <div>
     <h1>{{ Homepage }}</h1>
      <input type="file" ref="fileChoose" name="fileInput" value="Select File" @change="onFileSelected" style="display: none">
      <button @click="$refs.fileChoose.click()"> Choose File </button>
      <div>
        <button @click="onUpload" type="button-basic" name="button">Upload</button>
        <button @click="testAPIRes" type="button" name="button">Test API res</button>
      </div>
      <div id="preview">
        <img v-if="imageUrl" :src="imageUrl">
      </div>
     <!-- TODO:// Why isn't the image being sent. Only recieving none at endpoint. -->
   </div>
</template>

<style>
  body {
  background-color: var(--cl_background);
  }

  /* button {
  background-color: var(--cl_secondary);
  border: 3px solid black;
  color: var(--cl_text);
  padding: 1em 1.5em;
  text-align: center;
  text-decoration: none;
  font-size: 1.25em;
  display: inline-block;
  width: 15%; /* to test the test-align property */

  button{
  	background:linear-gradient(to bottom, var(--cl_secondary) 5%, #408c99 100%);
  	background-color:#599bb3;
  	border-radius:8px;
  	display:inline-block;
  	cursor:pointer;
  	color:#ffffff;
  	font-family:Arial;
  	font-size:20px;
  	font-weight:bold;
  	padding:13px 32px;
  	text-decoration:none;
  	text-shadow:0px 1px 0px #3d768a;
  }


#app {
  padding: 20px;
}

#preview {
  display: flex;
  justify-content: center;
  align-items: center;
}

#preview img {
  max-width: 100%;
  max-height: 500px;
}
</style>

<script>
  const axios = require('axios')
  export default {
    name: 'firstroute',
    data () {
      return {
      apiUrlBase: 'http://127.0.0.1:5000/',
      selectedFile: null,
      imageUrl: null,
    }
  },
  methods: {
    onFileSelected(event){
      const reader = new FileReader()
      console.log(event)
      this.selectedFile = event.target.files[0]
      console.log(this.selectedFile)
      // for the image preview.
      this.imageUrl = URL.createObjectURL(this.selectedFile)
    },
    onUpload(){
      const fd = new FormData();
      fd.append('imageName', this.selectedFile.name)
      fd.append('image', this.selectedFile)
      console.log("THIS SELECTED FILE = ")
      console.log(this.selectedFile)
      console.log(fd)
      axios.put('http://127.0.0.1:5000/upload_image', fd,{
          onUploadProgress: uploadEvent => {
            console.log('Upload Progress: ' + Math.round(uploadEvent.loaded / uploadEvent.total * 100) + '%')
          }
      })
        .then(res =>{
          console.log(res)
        })
        .catch((err) => {
          return new Error(err.message)
        })
    },
    testAPIRes(){
      axios.post('http://127.0.0.1:5000/hello_world/helloworld')
          .then(res =>{
            console.log(res)
        })
    }
  }
}
</script>
