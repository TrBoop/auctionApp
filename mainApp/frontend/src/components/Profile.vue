<template>
    <div class="profile">
        <br/>
    
    <div class="row justify-content-center align-items-center" style="min-width: 320px">
        <div class="col-5">
            <br/>
            <div class="border rounded bg-light p-5 ">
                <h1 class="h3 mb-4">Edit Profile</h1>
                <br/>
                <input type="file" accept="image/*" id="inputTitle" class="form-control" placeholder="Image"/>
                <br/>
                <input type="email" id="inputEmail" class="form-control" placeholder="Email address"/>
                <br/>
                <input type="text" id="inputUser" class="form-control" placeholder="Username"/>
                <br/>
                <input type="date" id="inputDOB" class="form-control"/>
                <br/>
                <input type="password" id="inputPassword" class="form-control" placeholder="Password" required />
                <br/>
                <div class="d-grid gap-2 col-8 mx-auto">
                    <button class="btn btn-primary" type="submit">Save Changes</button>
                </div>

            </div>
        </div>
    </div>

</div>
</template>