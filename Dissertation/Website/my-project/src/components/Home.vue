<template>
   <div>
     <h1>{{ Homepage }}</h1>
       Hello {{ $route.params.name }}
      <input type="file" name="fileInput" value="Select File" @change="onFileSelected">
      <button @click="onUpload" type="button" name="button">Upload</button>
      <button @click="testAPIRes" type="button" name="button">Test API res</button>
      <div id="preview">
        <img v-if="imageUrl" :src="imageUrl">
      </div>
     <!-- <div>
       <img :src="'../testImages/16Circles.jpg'">
     </div> -->
     <!-- TODO:// how to display images. Why isn't the image being sent -->
   </div>
</template>

<style scoped>
  body {
  background-color: #e2e2e2;
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
  const axios = require('Axios')
  export default {
    name: 'firstroute',
    data () {
      return {
      selectedFile: null,
      imageUrl: null
    }
  },
  methods: {
    onFileSelected(event){
      console.log(event)
      this.selectedFile = event.target.files[0]
      console.log(this.selectedFile)
      this.imageUrl = URL.createObjectURL(this.selectedFile)
    },

    onUpload(){
      const fd = new FormData();
      fd.append('imageName', this.selectedFile.name)
      fd.append('image', this.selectedFile)
      console.log(fd)
      axios.post('http://127.0.0.1:5000/upload_image', fd,{
          onUploadProgress: uploadEvent => {
            console.log('Upload Progress: ' + Math.round(uploadEvent.loaded / uploadEvent.total * 100) + '%')
          }
      })
        .then(res =>{
          console.log(res)
        })
    },

    onFileChange(event){
      const file = event.target.files[0]

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
