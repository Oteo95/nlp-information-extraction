import apollo from '@/js/apolloClient'
import get_document from '@/gql/get_doc.gql'
import mutate_tags from '@/gql/mutate_tags.gql'
import data from '@/config/config.js'

function initialState () {
  return {
    labels: data,
    document: undefined,
    is_loading: true,
    annotations: [],
    userannotations: [],
    mutating: false,
    runLabels: [],
  }
}

const state = initialState

const getters = {
  docText: (state) => {
    return state.document.text
  },
  sortAnnotations: (state) => {
    return state.annotations.slice().sort((a, b) => a.startOffset - b.startOffset)
  },
  labelObject: (state) => {
    const obj = {}
    for (const label of state.labels) {
      obj[label.id] = label
    }
    return obj
  },
  runLabels: (state) => {
    var runLabels = []
    for (const label of state.labels) {
      runLabels.push(label)
      }
    return runLabels
  },
}

const mutations = {
  document: (state, document) =>{
    state.document = document
  },
  updateStatus: (state, status) => {
    state.document.status = status
  },
  isLoading: (state, is_loading) => {
    state.is_loading = is_loading
  },
  updateAnnotation: (state, payload) => {
    state.annotations[payload.index].label = payload.labelId
    state.annotations[payload.index].annotatedby = payload.annotatedby
  },
  addAnnotation: (state, newAnnotation) => {
    state.annotations.push(newAnnotation)
  },
  updateAnnotations: (state, annotations) => {
    state.annotations = annotations
  },
  updateUserAnnotation: (state, userannotations) => {
    state.userannotations = userannotations
  },
  updateMutating: (state, mutating) => {
    state.mutating = mutating
  },
  reset (state) {
    const s = initialState()
    Object.keys(s).forEach(key => {
      state[key] = s[key]
    })
  }
}

const actions = {
  converAnnotationsFromAPI(context){
    var new_annotations =  []
    var annotations
    if (context.state.document.userannotations.length > 0) {
      annotations = context.state.document.userannotations
    } else {
      annotations = context.state.document.annotations
    }
    annotations.forEach(function (item, ) {
      const newAnnotation = {
        id: item.tagid,
        startOffset: item.start,
        endOffset: item.end,
        label: item.labelId,
        annotatedby: item.annotatedby,
        confidence: item.confidence
      }
      new_annotations.push(newAnnotation)
    });
    context.commit('updateAnnotations', new_annotations)
  },
  getDocument(context, doc_id){
    context.commit('reset')
    context.commit('isLoading', true)
    const variables = {
      "docid": doc_id
    }
    apollo.query({
      query: get_document,
      variables: variables,
      fetchPolicy: "no-cache",
    })
    .then(response => {
      context.commit('document', response.data.document)
      context.dispatch('converAnnotationsFromAPI')
      context.commit('isLoading', false)
    }).catch(error => {
      console.error(error);
      context.commit('isLoading', false)
    })
  },
  generateUserAnnotations(context){
    var user_annotations =  []
    context.state.annotations.forEach(function (item, ) {
      const pos = context.state.labels.map(
        function(e) { return e.id; }
      ).indexOf(item.label)
      const newAnnotation = {
        tagid: item.id,
        label: context.state.labels[pos].backText,
        start: item.startOffset,
        end: item.endOffset,
        labelId: item.label,
        annotatedby: item.annotatedby,
        confidence: item.confidence
      }
      user_annotations.push(newAnnotation)
    })
    context.commit('updateUserAnnotation', user_annotations)
  },
  addAnnotation(context, payload){
    var maxId = Math.max.apply(
      Math, context.state.annotations.map(function(o) { return o.id; })
    )
    if (maxId == -Infinity) {
      maxId = 0
    }
    const newAnnotation = {
      id: maxId + 1,
      startOffset: payload.startOffset,
      endOffset: payload.endOffset,
      label: payload.labelId,
      annotatedby: "user",
      confidence: 1,
    }
    context.commit('addAnnotation', newAnnotation)    
    context.dispatch('processAnnotations')
    return 
  },
  updateAnnotation(context, payload){
    const commitPayload = {
      index: context.state.annotations.findIndex(
        item => item.id === payload.annotationId
      ),
      labelId: payload.labelId,
      annotatedby: "user",
    }
    context.commit('updateAnnotation', commitPayload)
    context.dispatch('processAnnotations')
  },
  processAnnotations(context){
    context.dispatch('generateUserAnnotations')
    var variables = {
      docid: context.state.document.docid,
      userannotations: context.state.userannotations
    }
    context.commit('updateMutating', true)
    apollo.mutate({
      mutation: mutate_tags,
      variables: variables,
    })
    .then(response => {
      context.commit('updateStatus', response.data.updateAnnotations.status)
      context.commit('updateMutating', false)
    }).catch(error => {
      context.commit('updateMutating', false)
      console.error(error);
    });
  },
  deleteAnnotation(context, annotationId){
    const annotations = context.state.annotations.filter(
      item => item.id !== annotationId
    )    
    context.commit('updateAnnotations', annotations)
    context.dispatch('processAnnotations')
  },
}

export default {
  namespaced: true,
  state,
  getters,
  actions,
  mutations
}