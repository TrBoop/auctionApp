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
          <tr class="align-middle" v-for="auction in auctions" :key ="auction.itemFinishDate" @dblclick="$data.auction = auction">
              <td v-if="skippableDate(auction.itemFinishDate)">{{auction.itemTitle}} </td>
              <td v-if="skippableDate(auction.itemFinishDate)"><img src ={{auction.itemPicture}}/></td>
              <td v-if="skippableDate(auction.itemFinishDate)">{{auction.itemStartPrice}} </td>
              <td v-if="skippableDate(auction.itemFinishDate)">{{auction.itemFinishDate}}</td>
              <td v-if="skippableDate(auction.itemFinishDate)"><button type="button" class="btn btn-primary">Info</button></td>
              <div class="comments">
                <p></p>
              </div>  
          </tr>
          <p>Hello</p>
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
        questions: [],
        question:{
          'auctionId'
        },
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

      async getAuctions(){
        var response = await fetch("http://127.0.0.1:8000/api/auction/")
        let data = await response.json()
        this.auctions = data 
      },

      async addAuction(){
        await this.getAuctions();
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

      skippableDate(date){
            var now = new Date();
            var skippableDate = now.setDate(now.getDate())  // this is getting next thursday
	    var parseDate = Date.parse(date);

            if(parseDate > skippableDate){
                return true
            }else{
                return false
            }
        },


      }

  }
</script>