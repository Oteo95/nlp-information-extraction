<template>
  <div>
    <v-navigation-drawer
      app
      clipped
      permanent
      expand-on-hover
      width="170"
      class="white"
    >
      <v-list flat dense>
        <v-list-item-group active-class="border" color="green darken-2">
          <v-list-item v-for="link in links" :key="link.text" router :to="link.route">
            <v-list-item-icon>
              <v-icon>{{ link.icon }}</v-icon>
            </v-list-item-icon>
            <v-list-item-content>
              <v-list-item-title> {{ link.text }}</v-list-item-title>
            </v-list-item-content>
          </v-list-item>
        </v-list-item-group>
      </v-list>
    </v-navigation-drawer>

    <v-app-bar
      app
      clipped-left
      dense
      color="green-grey darken-4"
      dark
      flat
      fixed
      :hide-on-scroll="false"
    > 
      <v-img
        class="mr-5 ml-n2"
        src="logo/logo.png"
        max-height="75"
        max-width="100"
        contain
      ></v-img>
      <v-spacer></v-spacer>
      <span> Information Extraction</span>
    </v-app-bar>
  </div>

</template>

<script>
import {mapState} from 'vuex';

export default {
  data() {
    return {
      tag: undefined,
      drawer: false,
      links: [
        {icon: 'mdi-file-document-outline', text: 'Documents', route: '/'},
        {icon: 'mdi-format-textbox', text: 'Tagger', route: '/tagger' },
        // {icon: 'mdi-google-analytics', text: 'Analytics', route: '/analytics'},
      ]
    }
  },
  created(){
  },
  computed:{
    ...mapState([]),
    
  },
  methods: {
  },
}
</script>

<style scoped>
.border {
  border-left-width: 5px;
  border-left-style: solid;
  border-left-color: "green darken-2";
  padding-left: 11px;
}
</style>
