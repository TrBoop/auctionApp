<template>
    <div class="row h-100 justify-content-center align-items-center" style="min-width: 320px; min-height: 100vh">
        <div class="col-10 col-md-8 col-lg-4">
            <div class="border rounded bg-light shadow p-5">

                <h1 class="h3 mb-4">Register</h1>
                    <br/>
                    <input type="email" id="inputEmail" class="form-control" placeholder="Email address"/>
                    <br/>
                    <input type="text" id="inputUser" class="form-control" placeholder="Username"/>
                    <br/>
                    <input type="date" id="inputDOB" class="form-control"/>
                    <br/>
                    <input type="password" id="inputPassword" class="form-control" placeholder="Password" required />
                    <br/>
                    <div class="d-grid gap-2 col-6 mx-auto">
                        <button class="btn btn-primary" type="submit">Register</button>
                    </div>
                
                <p><br/>Already have an account?  <router-link to="/login" class="nav-link" style="color:blue; text-decoration:underline;">Sign In</router-link></p> 
            </div>
        </div>
    </div>
</template>