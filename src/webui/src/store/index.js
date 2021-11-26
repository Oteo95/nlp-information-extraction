import Vue from 'vue'
import Vuex from 'vuex'
//import createPersistedState from "vuex-persistedstate"

import router from '@/router/index.js' 
import apollo from '@/js/apolloClient'
import get_doc_list from '@/gql/get_doc_list.gql'
import tagger from '@/store/modules/tagger';


Vue.use(Vuex)

function initialState () {
  return {
    docs: undefined,
    currentDocId: undefined,
    rangeDates: [undefined, undefined],
  }
}

export default new Vuex.Store({
  strict: true,
  //plugins: [createPersistedState()],
  state: initialState,
  mutations: {
    docs: (state, docs) => {
      state.docs = docs
    },
    currentDocId: (state, doc_id) =>{
      state.currentDocId = doc_id
    },
  },
  actions: {
    
    tagDoc(context, doc_id){
      context.commit('currentDocId', doc_id)
      context.dispatch('tagger/getDocument', doc_id)
      router.push('/tagger')
    },
    get_doc_list(context) {
      apollo.query({
        query: get_doc_list,
        variables: {},
        fetchPolicy: "network-only",
      })
      .then(response => {
        var new_docs =  []
        var docs = response.data.documents
        docs.forEach(function (item, ) {
          const newDoc = {
            docid: item.docid,
            creation: item.creation,
            title: item.title,
            status: item.status,
          }
          new_docs.push(newDoc)
        });
        context.commit('docs', new_docs)
      });
    },
  },
  modules: {
    tagger
  },
})
