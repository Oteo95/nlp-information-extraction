<template>
    <v-data-table
      :headers="headers"
      :items="docs"
      :items-per-page="10"
      :loading="docs === undefined"
      loading-text="Loading docs..."
      class="mt-2 elevation-1"
    >
      <template v-slot:[`item.actions`]="{ item }">
        <v-tooltip top>
          <template v-slot:activator="{ on, attrs }">
            <v-icon
              small
              class="mr-n2"
              @click="annotate(item)"
              color="primary"
              v-bind="attrs"
              v-on="on"
            >
              mdi-pencil
            </v-icon>
          </template>
          <span>Edit</span>
        </v-tooltip>
      </template>
      <template v-slot:[`item.status`]="{ item }">
        <v-chip
          :color="getColorStatus(item.status)"
          small
          :outlined="item.status === 'loaded'? true: false"
          dark
        >
          {{statusMapping[item.status]}}
        </v-chip>
    </template>
  </v-data-table>
</template>

<script>
import {mapState, mapActions} from 'vuex';

export default {
  data(){
    return{
      menu: false,
      statusMapping: {
        'loaded': 'Loaded',
        'processed': 'Processed',
        'manual_processed': 'Modified',
      },
      headers: [
        {
          text: '',
          value: 'actions',
          sortable: false
        },
        {
          text: 'ID',
          value: 'docid',
          sortable: false,
          align: 'center',
          class: "subtitle-2 font-weight-bold"
        },
        {
          text: 'Status',
          value: 'status',
          align: 'center',
          class: "subtitle-2 font-weight-bold",
          width: '180',
        },
        {
          text: 'Date',
          value: 'creation',
          align: 'center',
          class: "subtitle-2 font-weight-bold",
          width: '180',
        },
        {
          text: 'Title', 
          value: 'title',
          align: 'center', 
          class: "subtitle-2 font-weight-bold",
        },
      ],
    }
  },
  created(){
    this.get_doc_list()
  },
  methods: {
    ...mapActions([
      'get_doc_list',
      'tagDoc',
    ]),

    annotate(item){
      console.log(item.docid)
      this.tagDoc(item.docid)
    },
    getColorStatus(status){
      if (status=='loaded') return '#757575'
      else if (status=='processed') return '#d1c17b'
      else if (status=='manual_processed') return '#79a4d2'
      else return '#757575'
    }
  },
  computed:{
    ...mapState([
      "docs",
    ]),
  }
}
</script>