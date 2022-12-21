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
</div>

</div>

<div v-for="auction in searchedAuctions" :key="auction.itemFinishDate" @dblclick="$data.auction = auction">
  <div class="row" v-if="skippableDate(auction.itemFinishDate)">
    <div class="col-5" style="">
      <div class="card card-body ">
        <img :src="auction.itemPicture.substring(39)" class="" width="200" max-height="300" style="margin-bottom:1rem; margin-left:auto; margin-right: auto;"/>
        <h5 class="card-title">{{auction.itemTitle}}</h5>
        <p class="card-text">{{auction.itemDescription}}</p>
        <h4 class="card-text">£{{auction.itemStartPrice}}</h4>
        <br/>
        <h6 class="card-text">Ends: {{auction.itemFinishDate}}</h6>
        <br/>
        <input type=number min="0" class="bg-light border border-black text-dark card-text" style="margin-bottom: 0.5rem; font-size:large;"/>
        <button type="button" class="btn btn-primary">Bid Amount</button>
      </div>
      
      <br/>
  
    </div>

    

    <br/>
    <div class="container col-7">
      <div class="card">
        
        <textarea class="bg-light border border-black text-dark"/>
        <button type="button" class="btn btn-primary" v-bind:id="'questionBox'+auction.questionId">Submit Question</button>
  
        <br/>
        <button type="button" class="btn btn-secondary" data-bs-toggle="collapse" data-bs-target="#collapseQuestion" aria-expanded="false" aria-controls="collapseQuestion">Show Questions</button>

          <div class="collapse" id="collapseQuestion" style="text-align:left" v-for="question in questions" :key="question.questionId">
            <br/>
            <h5 class="card-title">{{question.userId}}</h5>
            <p>
              {{question.questionText}}
            </p>

            <div v-for="answer in answers" :key="answer.answerId" style="margin-left:5rem;">
              <h6 class="card-title">{{answer.userId}}</h6>
              <p>
                {{answer.answerText}}
              </p>
            </div>

            <button type="button" class="btn btn-link" data-bs-toggle="collapse" data-bs-target="#collapseAnswer" aria-expanded="false" aria-controls="collapseAnswer" style="width:5rem; margin-left: auto;">Reply</button>
            <br/>
            <textarea class="bg-light border border-black text-dark collapse form-control" id="collapseAnswer"/>
            <button type="button" class="btn btn-primary collapse" id="collapseAnswer" style="margin-left:87%; width:13%;">Submit Answer</button>
          </div>

          
      </div>
    </div>
    <br/>
  </div>
  <br/>
</div>


</template>

<script>

import 'https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/js/bootstrap.bundle.min.js'
        
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