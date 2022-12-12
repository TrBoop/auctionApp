<template>
    <div class="row h-100 justify-content-center align-items-center" style="min-width: 320px; min-height: 100vh">
        <div class="col-10 col-md-8 col-lg-4">
            <div class="border rounded bg-light shadow p-5">
                <h1 class="h3 mb-4">Register</h1>
                <div class="row">
                    <div class="col">
                    <input type="text" class="form-control" placeholder="First name">
                    </div>
                    <div class="col">
                    <input type="text" class="form-control" placeholder="Last name">
                    </div>
                </div>
                <br/>
                <input type="email" id="inputEmail" class="form-control" placeholder="Email address"/>
                <br/>
                <input type="text" id="inputUser" class="form-control" placeholder="Username"/>
                <br/>
                <input type="password" id="inputPassword" class="form-control" placeholder="Password" required />
                <br/>
                <input type="password" id="confirmPassword" class="form-control" placeholder="Confirm Password" required />
                <br/>
                <div class="d-grid gap-2 col-6 mx-auto">
                    <button class="btn btn-primary" type="submit">Register</button>
                </div>
                
                <!-- The a href needs to be replaced by a router -->
                <p><br/>Already have an account? <a href="#!">Sign In</a></p> 
            </div>
        </div>
    </div>
</template>