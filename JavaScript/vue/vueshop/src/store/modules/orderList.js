import Vue from 'vue'

const state = {
  orderList: [],
  params: {}
}

const getters = {
  getOrderList (state) {
    return state.orderList
  }
}

const actions = {
  fetchOrderList ({ commit, state }) {
    Vue.http.get('/api/getOrderList', state.params)
      .then((res) => {
        commit('updateOrderList', res.data.list)
      }, (err) => {
        console.log(err)
      })
  }
}

const mutations = {
  updateOrderList (state, payload) {
    state.orderList = payload
  },
  updateParams (state, { key, val }) {
    state.params[key] = val
    console.log(state.params)
  }
}

export default {
  state,
  getters,
  actions,
  mutations
}
