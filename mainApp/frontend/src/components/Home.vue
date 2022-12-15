<template >

<div class="home">
    <br/>
<h1> Listings </h1>
<div class="d-grid gap-2 col-6 mx-auto">
    <button class="btn btn-primary" type="submit"> <router-link to="/newitem" class="nav-link">New Item</router-link></button>
</div>
<br/>
<div class="row">

<table class="table table-striped border rounded bg-light shadow">
        <thead>
          <tr>
            <th scope="col">Item Title</th>
            <th scope="col">Image</th>
            <th scope="col">Start Price</th>
            <th scope="col">Ending</th>
          </tr>
        </thead>
        <tbody>
          <tr class="align-middle">
            <td> </td>
            <td> </td>
            <td> </td>
            <td> </td>
            <td><button type="button" class="btn btn-primary">Info</button></td>
          </tr>
        </tbody>
      </table>

</div>

</div>
</template>