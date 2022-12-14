<script setup>
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <div>
    <a href="https://vitejs.dev" target="_blank">
      <img src="/vite.svg" class="logo" alt="Vite logo" />
    </a>
    <a href="https://vuejs.org/" target="_blank">
      <img src="./assets/vue.svg" class="logo vue" alt="Vue logo" />
    </a>
  </div>
  <HelloWorld msg="Vite + Vue" />
</template>

<script>
  export default{
    name: 'App',
    data(){
      return{
        users: [],
        user:{
          'userPassword': '',
          'username': '',
          'userEmail': '',
          'userDateOfBirth': '',
          'userImage': '', 
        }
      } 
    },

    async created(){
       await this.getUsers();
      },
    methods:{

      submitUser(){
        if(this.user.id ===undefined){
          this.addUser();
        }
        else{
          this.updateUser();
        }
      },

      async getUsers(){
        var response = await fetch("http://127.0.0.1:8000/api/records/")
        let data = await response.json()
        this.users = data 
      },

      async addUser(){
        await this.getUsers();
        await fetch("http://127.0.0.1:8000/api/records/",{
          method: 'post',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.record)  
        });
        await this.getUsers();
        this.user = {};
      },

      async updateUser(){
        await this.getUsers();
        await fetch(`http://127.0.0.1:8000/api/records/${this.record.id}/`,{
          method: 'put',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.record)  
        });
        await this.getUsers();
        this.user = {};
      },

      async deleteUser(user){
        await this.getUsers();
        await fetch(`http://127.0.0.1:8000/api/records/${user.id}/`,{
          method: 'delete',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.record)  
        });
        await this.getUsers();
      }
    }
  }
</script>