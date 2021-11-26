<template>
    <v-container
      fluid
      fill-height 
      class="pa-0 mb-10 grey lighten-4"
    >      
      <Loading v-if="is_loading" />

      <v-layout v-else
        row wrap justify-space-around
      >
        <v-flex xs12 md10>
          <v-layout row wrap justify-space-around>
            <v-flex class="mt-8" xs11 lg12>
              <v-row>
                <v-btn
                  text
                  color="primary"
                  plain
                  @click="movePrevDoc()"
                >
                  <v-icon left>
                    mdi-arrow-left-bold
                  </v-icon>
                  Prev Document
                </v-btn>
                <v-spacer></v-spacer>
                <v-btn
                  text
                  color="primary"
                  plain
                  @click="moveNextDoc()"
                >
                  Next Document
                  <v-icon right>mdi-arrow-right-bold</v-icon>
                </v-btn>
              </v-row>
            </v-flex>
            <v-flex class="mt-4" xs11 lg12>
              <v-card class="mb-10">
                <v-card-title class="center-justified" style="font-size: 17px">
                  {{document.title}}
                  <v-icon
                    v-if="document.status === 'confirmed'"
                    class="ml-2 mt-n1"
                    dark 
                    color="teal"
                  > mdi-check-circle
                  </v-icon>
                  <v-card-subtitle class="mt-n5 mb-n5 center-justified" style="font-size: 12px">
                    (<span class="font-weight-bold" >ID:</span> {{document.docid}},
                    <span class="font-weight-bold">Time:</span> {{document.creation}})
                  </v-card-subtitle>
                </v-card-title>
                <v-card-text>
                  <v-layout row wrap justify-space-around>
                    <v-flex class="mt-2 mb-8" xs11 lg7 xl8>
                      <v-card flat outlined>
                        <v-card-text class="my-list">
                          <AnnotationItemBox />
                        </v-card-text>
                      </v-card>
                    </v-flex>
                  </v-layout>
                </v-card-text>
              </v-card>
            </v-flex>
          </v-layout>
        </v-flex>
      </v-layout>
    </v-container>
</template>

<script>
import {mapState, mapActions} from 'vuex';

import AnnotationItemBox from '@/components/tagging/AnnotationItemBox.vue'
import Loading from '@/components/tagging/Loading.vue'


export default {
  name: 'tagging',
  components: {
    AnnotationItemBox,
    Loading
  },
  computed: {
    ...mapState("tagger", [
      "document",
      "is_loading",
    ]),

  },
  methods: {
    ...mapActions([
      'moveNextDoc',
      'movePrevDoc',
    ]),
  },
}
</script>

<style scoped>
  .my-list {
    height: calc(130vh - 275px);
    overflow-y: auto;
  }
  .center-justified {
    display: block;
    text-align: center;
    text-justify: center;
    -moz-text-align-last: center;
    text-align-last: center;
    word-break: normal
  }
</style>