import axios from 'axios';

const state = {
  products: []
};

const getters = {
  allProducts: state => state.products
};

const actions = {
  async fetchProducts({ commit }) {
    const response = await axios.get(

      // 'https://jsonplaceholder.typicode.com/todos',
      'http://127.0.0.1:8000/business/products/',
      
      {
        params: {
          _limit: 5
         }
      }
    );

    commit('setProducts', response.data);
  },
  async addProduct({ commit }, title) {
    const response = await axios.post(
      'https://jsonplaceholder.typicode.com/todos',
      { title, completed: false }
    );

    commit('newProduct', response.data);
  },
  async deleteProduct({ commit }, id) {
    await axios.delete(`http://127.0.0.1:8000/business/products/${id}`);

    commit('removeProduct', id);
  },
  // async filterTodos({ commit }, e) {
  //   // Get selected number
  //   const limit = parseInt(
  //     e.target.options[e.target.options.selectedIndex].innerText
  //   );

  //   const response = await axios.get(
  //     `https://jsonplaceholder.typicode.com/todos?_limit=${limit}`
  //   );

  //   commit('setTodos', response.data);
  // },
  async updateProduct({ commit }, updProduct) {
    // 500ari varaei
    const response = await axios.patch(
      `http://127.0.0.1:8000/business/products/${updProduct.id}/`,
      updProduct
    )
    .then((response) => {
      console.log(response);
    }, (error) => {
      console.log(error);
    });
    commit('updateProduct', response.data);
  }
};

const mutations = {
  setProducts: (state, products) => (state.products = products),
  newProduct: (state, product) => state.products.unshift(product),
  removeProduct: (state, id) => (state.products = state.products.filter(product => product.id !== id)),
  updateProduct: (state, updProduct) => {
    const index = state.products.findIndex(product => product.id === updProduct.id);
    if (index !== -1) {
      state.products.splice(index, 1, updProduct);
    }
    else{
      console.log('ERRORR')
    }
  }
};

export default {
  state,
  getters,
  actions,
  mutations
};
