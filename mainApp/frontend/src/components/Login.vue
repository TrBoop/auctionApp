<template>
    <div class="row h-100 justify-content-center align-items-center" style="min-width: 320px; min-height: 100vh">
        <div class="col-10 col-md-8 col-lg-4">
            <div class="border rounded bg-light shadow p-5 ">
                <h1 class="h3 mb-4">Sign In</h1>
                <input type="email" id="inputEmail" class="form-control" placeholder="Email address"/>
                <br/>
                <input type="password" id="inputPassword" class="form-control" placeholder="Password" required />
                <br/>
                <div class="d-grid gap-2 col-6 mx-auto">
                    <button class="btn btn-primary" type="submit">Sign In</button>
                </div>
                
                <!-- The a href needs to be replaced by a router -->
                <p><br/>Not a member? <a href="#!">Register</a></p> 
            </div>
        </div>
    </div>
</template>