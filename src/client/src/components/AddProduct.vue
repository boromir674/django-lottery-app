<template>
  <div>
    <h3>Add Product</h3>
    <div class="add">
      <form @submit="onSubmit">
        <input type="text" v-model="title" style="width: 100px;" placeholder="Product Name">
        <b-button variant="outline-success" type="submit">Success</b-button>
      </form>
    </div>
  </div>
</template>

<script>
import { mapActions } from "vuex";
export default {
  name: "AddProduct",
  data() {
    return {
      title: ""
    };
  },
  methods: {
    ...mapActions(["addProduct"]),
    onSubmit(e) {
      e.preventDefault();
      this.addProduct(this.title);
    }
  }
};
</script>

<style scoped>
form {
  display: flex;
}

input[type="text"] {
  flex: 5;
  padding: 10px;
  border: 1px solid #41b883;
  outline: 0;
}

input[type="submit"] {
  flex: 2;
  background: #41b883;
  color: #fff;
  border: 1px #41b883 solid;
  cursor: pointer;
}
</style>
