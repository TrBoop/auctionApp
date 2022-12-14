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
        if(this.record.id ===undefined){
          this.addUser();
        }
        else{
          this.updateUser();
        }
      },

      async getUsers(){
        var response = await fetch("http://127.0.0.1:8000/api/records/")
        let data = await response.json()
        this.records = data 
      },

      async addUser(){
        await this.getUsers();
        await fetch("http://127.0.0.1:8000/api/records/",{
          method: 'post',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.user)  
        });
        await this.getUsers();
        this.user = {};
      },

      async updateUser(){
        await this.getUsers();
        await fetch(`http://127.0.0.1:8000/api/records/${this.user.id}/`,{
          method: 'put',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.record)  
        });
        await this.getUSers();
        this.record = {};
      },

      async deleteUser(user){
        await this.getRecords();
        await fetch(`http://127.0.0.1:8000/api/records/${user.id}/`,{
          method: 'delete',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.user)  
        });
        await this.getUsers();
      }
    }
  }
</script>

<template>
  <Navbar/>
  <router-view :key="$route.path" />
</template>

<style scoped>
.logo {
  height: 6em;
  padding: 1.5em;
  will-change: filter;
}
.logo:hover {
  filter: drop-shadow(0 0 2em #646cffaa);
}
.logo.vue:hover {
  filter: drop-shadow(0 0 2em #42b883aa);
}
</style>
