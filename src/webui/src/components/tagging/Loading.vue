<template>
      <v-layout row wrap justify-space-around
      >
        <v-flex xs12 md10 xl8>
          <v-card v-if="currentDocId === undefined" class="mt-10" flat color='rgba(0,0,0,0)'>
            <v-card-title primary-title class="justify-center">
              Please, select a document first
            </v-card-title>
            <v-card-actions class="mt-8">
              <v-layout row justify-center>
                <v-btn 
                  tile
                  text
                  color="primary"
                  to="/"
                >
                  <v-icon left>
                    mdi-arrow-left-bold
                  </v-icon>
                  Go to documents
                </v-btn>
              </v-layout>
            </v-card-actions>
          </v-card>
          <v-card v-else class="mt-10">
            <v-layout row wrap justify-space-around>
              <v-flex xs11 sm10 md11>
                <v-row class="mx-n7">
                </v-row>
              </v-flex>
              <v-flex class="my-5 mx-5" xs11 sm10 md7>
                <v-skeleton-loader
                  flat
                  type="list-item-three-line@3"
                >
                </v-skeleton-loader>
              </v-flex>
              <v-flex class="my-5 mx-5" xs11 sm10 md4>
                <v-skeleton-loader
                  flat
                  type="list-item-two-line@3"
                ></v-skeleton-loader>
              </v-flex>
            </v-layout>
          </v-card>
        </v-flex>
      </v-layout>

</template>

<script>
import {mapState} from 'vuex';


export default {
  name: 'Loading',
  components: {
  },
  computed: {
    ...mapState([
      "currentDocId",
    ]),
  },
}
</script>
