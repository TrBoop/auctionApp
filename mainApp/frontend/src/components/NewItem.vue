<template>
     <div class="row justify-content-center" style="min-width: 320px; min-height: 100vh; margin-top: 3rem;">
        <div class="col-10 col-md-8 col-lg-8">
            <div class="border rounded bg-light shadow p-5">
                <h1 class="h3 mb-4">New Item</h1>
                    <br/>
                    <input type="text" id="inputTitle" class="form-control" placeholder="Title"/>
                    <br/>
                    <textarea id="inputDescription" class="form-control" placeholder="Item Description"/>
                    <br/>
                    <input type="file" accept="image/*" id="inputTitle" class="form-control" placeholder="Image"/>
                    <br/>
                    <input type="date" id="inputEnd" class="form-control"/>
                    <br/>
                    <input type="number" id="inputStartPrice" class="form-control" placeholder="Starting Price" required />
                    <br/>
                    <div class="d-grid gap-2 col-6 mx-auto">
                        <button class="btn btn-primary" type="submit">Submit Item</button>
                    </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default{
        name: 'NewItem',
        data(){
            return{
                newAuction:{
                    'itemTitle':'',
                    'itemDescription':'',
                    'itemStartPrice':'',
                    'itemPicture': '',
                    'itemFinishDate':'',
                    'ownerId':'',      
                }
            }
        },
        methods:{ 
        } 
    }


</script>