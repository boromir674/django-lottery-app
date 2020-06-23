<template>
  <div>
    <h3>Products</h3>
    <div class="products">
      <div
        @dblclick="onDblClick(product)"
        v-for="product in allProducts"
        :key="product.id"
        class="product"
      >
         <b-card     
          img-src="https://picsum.photos/600/300/?image=25"
          img-width=150
          img-alt="Image"
          img-top
          tag="article"
          style="max-width: 20rem;"
          class="mb-2"
          :class="{'is-complete':product.completed}"
          >
          <div v-if="editable === product.id">
              <b-card-title ><b-form-input :value="product.name"/></b-card-title>      
              <b-form-textarea
                  id="description"
                  :value="product.description"
                  :placeholder="product.description"
                  rows="4"
                  max-rows="6"
                  size="md"
                />
          </div>
          <div v-else>
              <b-card-title >{{product.name}}</b-card-title>
          </div>
          
          <div style="display:inline-flex;">
              <span class="price">
              <span class="sign">$</span>
              <span class="currency">{{product.value}}</span>
              </span>
              <i @click="deleteProduct(product.id)" class="fas fa-trash-alt" />
              <b-form-checkbox
                @change="edit_product(product)" 
                name="check-button" 
                :key= "product.id"
                :checked="editable === product.id"
                switch
              />
        </div>
        </b-card>
      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters, mapActions } from "vuex";

export default {
  name: "Products",
  data() {
    return {
      name:'',
      description: '',
      editable: 0,
      status: ''
    };
  },
  methods: {
    ...mapActions(["fetchProducts", "deleteProduct", "updateProduct"]),
    // onDblClick(todo) {
    //   const updTodo = {
    //     id: todo.id,
    //     title: todo.title,
    //     completed: !todo.completed
    //   };

    //   this.updateTodo(updTodo);
    // },
    edit_product: function(product){
     console.log(this.editable )
      if(product.id !== this.editable){
        this.editable = product.id;
      }else{
        this.editable = 0;
        // EDIT HERE
      
      // const updTodo = {
      //   id: todo.id,
      //   title: todo.title,
      //   completed: !todo.completed
      // };

      // this.updateTodo(updTodo);
      }
    },
    editProduct(product){
        const updProduct = {
        id: product.id,
        name: product.name,
        description: product.description,
        value: 15,
     };
      this.updateProduct(updProduct);
  
    },
    insert_name: function(message) {
      this.name = message
      // console.log(this.name)
    },
    insert_desc: function(message) {
      this.description = message
      // console.log(this.description)
    },
      

    // insert_field: function(message, type, todo) {
    //   // (type === 'name') ?  this.name = message : this.description = message;
    //   // console.log(message)
      
    //   if (type === 'title'){
    //     this.name = message
    //     console.log(this.name)
    //   } else {
    //     this.description = message
    //     console.log(this.description)
    //   }
    // }
  },
  computed: mapGetters(["allProducts"]),
  created() {
    this.fetchProducts();
  }
};
</script>

<style scoped>
.products {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  grid-gap: 0.2rem;
}


.price .currency {
    font-family: "Lato",sans-serif;
    font-size: 30px;
    font-weight: 300;
    letter-spacing: -2px;
    line-height: 40px;
    vertical-align: middle;
} 
 
 /* .fa-trash-alt {
  position: absolute;
  bottom: 10px;
  right: 10px;
  color: #fff;
  cursor: pointer;
}

.fa-toggle-off{
  position: absolute;
  bottom: 10px;
  left: 10px;
  color: #fff;
  cursor: pointer;
} */


@media (max-width: 300px) {
  .products {
    grid-template-columns: 1fr;
  }
}
</style>
