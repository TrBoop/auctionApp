<template>
    <div class="row h-100 justify-content-center align-items-center" style="min-width: 320px; min-height: 100vh">
        <div class="col-10 col-md-8 col-lg-4">
            <div class="border rounded bg-light shadow p-5">

                <h1 class="h3 mb-4">Register</h1>
                    <br/>
                    <form @submit.prevent="handleSubmit">
                    <input type="email" v-model="inputEmail" class="form-control" placeholder="Email address"/>
                    <br/>
                    <input type="text" v-model="inputUser" class="form-control" placeholder="Username"/>
                    <br/>
                    <input type="date" v-model="inputDOB" class="form-control"/>
                    <br/>
                    <input type="password" v-model="inputPassword" class="form-control" placeholder="Password" required />
                    <br/>
                    <p v-if="errorEmail">Email already in use</p>
                    <p v-if="errorEmail2">Not valid email</p>
                    <p v-if="errorUser">Username in use</p>
                    <p v-if="errorDOB">DOB wrong format</p>
                    <div class="d-grid gap-2 col-6 mx-auto">
                        <button class="btn btn-primary" type="submit">Register</button>
                    </div>
                    </form>
                
                <p><br/>Already have an account?  <router-link to="/login" class="nav-link" style="color:blue; text-decoration:underline;">Sign In</router-link></p> 
            </div>
        </div>
    </div>
</template>

<script>

    export default {
        name: 'Register',
        data() {
            return {
                inputPassword: '',
                inputUser: '',
                inputDOB: '',
                inputPassword: '',
                errorEmail: false,
                errorUser: false,
                errorDOB: false,
                errorInvalidEmail: false,
            }
        },
        methods: {

             async handleSubmit(){
                this.errorEmail = false;
                this.errorUser = false;
                this.errorDOB = false;
                this.errorInvalidEmail = false;

                const inputdata = {
                    userEmail: this.inputEmail,
                    username: this.inputUser,
                    userDateOfBirth: this.inputDOB,
                    userPassword: this.inputPassword,
                };
                console.log(inputdata);

                let response = await fetch("http://127.0.0.1:8000/api/users/",{
                  method: 'post',
                  headers: {
                    'Content-Type': 'application/json'
                  },
                  body: JSON.stringify(inputdata)  
                });
                let data2 = await response.json();
                console.log(data2);

                this.$router.push('/login');

                if (data2.userEmail["0"] == 'User with this userEmail already exists.'){
                    this.errorEmail = true;
                }
                if (data2.userEmail["0"] == 'Enter a valid email address.'){
                    this.errorInvalidEmail = true;
                }
                if (data2.username["0"] == 'User with this username already exists.'){
                    this.errorUser = true;
                }
                if (data2.userDateOfBirth["0"] == 'Date has wrong format. Use one of these formats instead: YYYY-MM-DD.') {
                    this.errorDOB = true;
                }   
                       
        }
    }
    }

</script>
