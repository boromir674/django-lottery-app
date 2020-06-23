<template>
  <div id="app">
    
    <b-container fluid="md">
      <!-- <HomePage/> -->
      <AddProduct/>
      <Products/>
    </b-container>
    
    
    
    
    <!-- <div class="container"> -->
    <!-- 
      <AddProduct/>
      <!-- <FilterTodos/> 
      <Products/>
    -->
    <!-- <HomePage/>
    </div> -->

  </div>
</template>

<script>
import HomePage from "./components/HomePage.vue";
import Products from "./components/Products.vue";
import AddProduct from "./components/AddProduct.vue";
import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap-vue/dist/bootstrap-vue.css";
// import FilterTodos from "./components/FilterTodos.vue";


export default {
  name: "app",
  components: {
    // HomePage
    Products,
    AddProduct
    // FilterTodos
  }
};
</script>

<style>
body {
  font-family: "Franklin Gothic Medium", "Arial Narrow", Arial, sans-serif;
  line-height: 1.6;
  background: #e8f7f0;
  /* background-image: url(require('../assets/lottery.jpg')); */
}
/* .container {
  max-width: 600px;
  margin: auto;
  overflow: off;
  padding: 0 2rem;
} */
</style>
