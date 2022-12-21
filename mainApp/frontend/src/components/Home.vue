<template >

<div class="home">
    <br/>
<h1> Listings </h1>
<div class="d-grid gap-2 col-6 mx-auto">
    <button class="btn btn-primary" type="submit"> <router-link to="/newitem" class="nav-link">New Item</router-link></button>
</div>
<br/>
<div class="row">
  <div class="input-group" style="margin-bottom:1rem;">
    <input type="search" class="form-control rounded" placeholder="Search" id="search" v-on:input="searchItem()" />
    <button type="button" class="btn btn-outline-primary">Search</button>
  </div>
  
<table class="table border rounded bg-light shadow">
        <thead>
          <tr>
            <th scope="col">Item Title</th>
            <th scope="col">Item Description</th>
            <th scope="col">Image</th>
            <th scope="col">Start Price</th>
            <th scope="col">Ending</th>
          </tr>
        </thead>
        <tbody class="align-middle" v-for="auction in searchedAuctions" :key="auction.itemFinishDate" @dblclick="$data.auction = auction" >
          <tr style="background:#E1E1E1;" v-if="skippableDate(auction.itemFinishDate)" >
              <td>{{auction.itemTitle}} </td>
              <td>{{auction.itemDescription}} </td>
              <td><img :src="auction.itemPicture.substring(39)" width="100"/></td>
              <td>{{auction.itemStartPrice}} </td>
              <td>{{auction.itemFinishDate}}</td>
              <td></td>
              <td>
                <tr><input type=number min="0" class="bg-light border border-light text-dark" style="margin-bottom: 0.5rem;"/></tr>
                <tr><button type="button" class="btn btn-primary">Bid Amount</button></tr>
              </td>
              <td>
                <tr><textarea class="bg-light border border-light text-dark"/></tr>
                <tr><button type="button" class="btn btn-primary">Submit Question</button></tr>
              </td>
              
              <td><router-link v-bind:to="item." class="nav-link">More Info</router-link></td>
          </tr>
          
    
          <tr v-if="skippableDate(auction.itemFinishDate)"> 
            <th></th> <!-- Leave Empty -->
            <th scope="col">Questions</th>
          </tr>
          <tr v-if="skippableDate(auction.itemFinishDate)">
            <th></th> <!-- Leave Empty -->
            <th scope="col">User</th>
            <th scope="col">Question</th>
          </tr>
          
          <tr v-for="question in questions" :key="question.questionId" v-if="skippableDate(auction.itemFinishDate)">  
            <td></td> <!-- Leave Empty -->
            <td>{{question.userId}}</td> <!-- GET Userid from question -->
            <td>{{question.questionText}}</td> <!-- GET question from question -->
    
            

            <tr>
              <th></th> <!-- Leave Empty -->
              <th></th> <!-- Leave Empty -->
              <th scope="col">Answer</th>

            </tr>

            <tr v-for="answer in answers" :key="answer.answerId">
              <td></td> <!-- Leave Empty -->
              <td></td> <!-- Leave Empty -->
              <td>{{answer.answerText}}</td> 
              <td></td> <!-- Leave Empty -->
              
              
              <td>
                <tr><textarea class="bg-light border border-light text-dark"/></tr>
                <tr><button type="button" class="btn btn-primary">Submit Answer</button></tr>
              </td>
            </tr>

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
        questions: [],
        question:{
          'auctionId':'',
          'questionText':'',
          'userId':'',
        },
        answers:[],
        answer:{
          'questionId': '',
          'answerText': '',
          'userId': '',
        },
        auctions: [],
        searchedAuctions: [],
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
       await this.getQuestions();
       await this.getAnswers();
      },
      methods:{

      async getAuctions(){
        var response = await fetch("http://127.0.0.1:8000/api/auction/")
        let data = await response.json()
        this.auctions = data 
        this.searchedAuctions = data
      },

      async getQuestions(){
        var response = await fetch("http://127.0.0.1:8000/api/question/")
        let data = await response.json()
        this.questions = data 
      },

      async getAnswers(){
        var response = await fetch("http://127.0.0.1:8000/api/answer/")
        let data = await response.json()
        this.answers = data 
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

        searchItem(){ 
          var searchedAuction =document.getElementById('search').value; 
          this.searchedAuctions = this.auctions.filter(auction => auction.itemTitle.toLowerCase().includes(searchedAuction) || auction.itemDescription.toLowerCase().includes(searchedAuction)); 
        },

      }

  }

  
 
</script>