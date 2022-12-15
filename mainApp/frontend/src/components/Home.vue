<template >

<div class="home">
    <br/>
<h1> Listings </h1>
<div class="d-grid gap-2 col-6 mx-auto">
    <button class="btn btn-primary" type="submit"> <router-link to="/newitem" class="nav-link">New Item</router-link></button>
    <button class="btn btn-primary" type="submit" @click="getAuctions()" >display</button>
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
          <tr class="align-middle" v-for="auction in auctions" :key ="auction.itemFinishDate" @dblclick="$data.auction = auction" >
            <td>{{auction.itemTitle}} </td>
            <td>{{auction.itemPicture}} </td>
            <td>{{auction.itemStartPrice}} </td>
            <td>{{itemFinishDate}} </td>
            <td><button type="button" class="btn btn-primary">Info</button></td>
          </tr>
        </tbody>
      </table>

</div>

</div>
</template>

<script>
  export default{
    name: 'Home',
    data(){
      return{
        auctions: [],
        auction:{
          'itemTitle':'',
          'itemDescription':'',
          'itemStartPrice':'',
          'itemPicture': '',
          'itemFinishDate':'',
          'ownerId':'',  
        }
      }
    },
    async created(){
       await this.getAuctions();
      },
      methods:{
        submitAuction(){
        if(this.auction.id ===undefined){
          this.addAuction();
        }
        else{
          this.updateAuction();
        }
      },

      async getAuctions(){
        var response = await fetch("http://127.0.0.1:8000/api/auction/")
        let data = await response.json()
        this.auctions = data 
      },

      async addAuction(){
        await this.getAuction();
        await fetch("http://127.0.0.1:8000/api/auction/",{
          method: 'post',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.auction)  
        });
        await this.getAuctions();
        this.auction = {};
      },

      async updateAuction(){
        await this.getAuctions();
        await fetch(`http://127.0.0.1:8000/api/auction/${this.auction.id}/`,{
          method: 'put',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.auction)  
        });
        await this.getAuctions();
        this.auction = {};
      },

      async deleteAuction(auction){
        await this.getAuctions();
        await fetch(`http://127.0.0.1:8000/api/auction/${auction.id}/`,{
          method: 'delete',
          headers: {
            'Content-Type': 'application/json'
          },
          body: JSON.stringify(this.auction)  
        });
        await this.getAuctions();
      },  
      }

  }
</script>