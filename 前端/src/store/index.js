import Vue from 'vue'
import Vuex from 'vuex'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    changedCurrent: "",
    indexData: "",
    videoInfo: {title: 'a'},
  },
  mutations: {
    getChangedCurrent: function (state, changedCurrent) {
      state.changedCurrent = changedCurrent;
    },
    getIndexData: function (state, indexData) {
      state.indexData = indexData;
    },
    getVideoInfo: function (state, videoInfo) {
      state.videoInfo = videoInfo
    }

  },
  actions: {
  },
  modules: {
  }
})
