<template>
   <div>
     <h1>{{ Homepage }}</h1>
       Hello {{ $route.params.name }}
      <input type="file" name="fileInput" value="Select File" @change="onFileSelected">
      <button @click="onUpload" type="button" name="button">Upload</button>
      <button @click="testAPIRes" type="button" name="button">Test API res</button>
     <!-- <div>
       <img :src="'../testImages/16Circles.jpg'">
     </div> -->
     <!-- TODO:// how to display images. Why isn't the image being sent -->
   </div>
</template>
<script>
  const axios = require('Axios')
  export default {
    name: 'firstroute',
    data () {
      return {
      selectedFile: null
    }
  },
  methods: {
    onFileSelected(event){
      console.log(event)
      this.selectedFile = event.target.files[0]
      console.log(this.selectedFile)
    },
    onUpload(){
      const fd = new FormData();
      // fd.append('image', this.selectedFile, this.selectedFile.name)
      fd.append('imageName', this.selectedFile.name)
      fd.append('image', this.selectedFile)
      console.log(fd)
      axios.put('http://127.0.0.1:5000/upload_image', fd,{
          onUploadProgress: uploadEvent => {
            console.log('Upload Progress: ' + Math.round(uploadEvent.loaded / uploadEvent.total * 100) + '%')
          }
      })
        .then(res =>{
          console.log(res)
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
