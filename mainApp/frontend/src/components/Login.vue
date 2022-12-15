<template>
    <div class="row h-100 justify-content-center align-items-center" style="min-width: 320px; min-height: 100vh">
        <div class="col-10 col-md-8 col-lg-4">
            <div class="border rounded bg-light shadow p-5 ">
                <h1 class="h3 mb-4">Sign In</h1>
                <form @submit.prevent="handleSubmit">
                <input type="email" v-model="userLogin.inputEmail" class="form-control" placeholder="Email address"/>
                <br/>
                <input type="password" v-model="userLogin.inputPassword" class="form-control" placeholder="Password" required />
                <br/>
                <div class="d-grid gap-2 col-6 mx-auto">
                    <button class="btn btn-primary" type="submit">Sign In</button>
                </div>
                </form>
                <p><br/>Not a member? <router-link to="/register" class="nav-link" tag="button" style="color:blue; text-decoration:underline;">Register</router-link></p>
                

                
                
            </div>
        </div>
    </div>
</template>

<script>
    export default {
            name: 'Login',
            data(){
                return {
                    userLogin:{
                        inputEmail: '',
                        inputPassword:'',   
                    }
                }
            },
            methods:{
                async handleSubmit() {
                    const data = {
                        userEmail: this.inputEmail,
                        userPassword: this.inputPassword,
                    };
                    console.log(data);

                    let response = await fetch("http://127.0.0.1:8000/api/users/",{
                      method: 'get',
                      headers: {
                        'Content-Type': 'application/json'
                      },
                      body: JSON.stringify(data)  
                    })
                    let data2 = await response.json();
                    console.log(data2);

                }
            }
        }
</script>