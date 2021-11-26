<template>
  <v-menu
      v-if="chunk.label"
      v-model="showMenu"
      offset-y
  >
    <template v-slot:activator="{ on: menu }">
      <span 
        :id="'spn-' + chunk.id"
        :style="borderStyle"
        class="highlight bottom"
        v-on="{...menu }"
      >
        <span class="highlight__content">{{ chunk.text }}<span
        ><v-icon class="delete" @click.stop="deleteAnnotation(chunk.id)">mdi-close</v-icon></span>
      
        <span>
          <v-tooltip
            bottom 
          >
            <template v-slot:activator="{ on: tooltip }">
            <span
                  :data-label="chunk.label"
                  :style="{ 'backgroundColor': chunk.color}"
                  class="highlight__rest-labels"
                  v-on="{...tooltip }"
                />
              </template>
            <span>{{ (chunk.confidence * 100).toFixed(0) }}%</span>
          </v-tooltip>
        </span>
    </template>
    <span>{{ (chunk.confidence * 100).toFixed(0) }}%</span>
    
    
    <v-list
        dense
        min-width="150"
        max-height="400"
        class="overflow-y-auto"
    >
      <v-list-item
          v-for="(item, i) in labels"
          :key="i"
          v-shortkey.once="[item.suffixKey]"
          @shortkey="updateAnnot(item)"
          @click="updateAnnot(item)"
      >
        <v-list-item-content>
          <v-list-item-title v-text="item.text"/>
        </v-list-item-content>
        <v-list-item-action>
          <v-list-item-action-text v-text="item.suffixKey"/>
        </v-list-item-action>
      </v-list-item>
    </v-list>
  </v-menu>

  <span v-else :class="[chunk.newline ? 'newline' : '']">{{ chunk.text }}</span>
</template>

<script>
import {mapState, mapActions} from 'vuex';

export default {
  props: {
    chunk: {
      type: Object,
      required: true
    },
  },

  data() {
    return {
      showMenu: false,
    }
  },

  computed: {
    ...mapState("tagger", [
      "labels",
    ]),
    borderStyle(){
      var borderStyle
      if (this.chunk.annotatedby === "model"){
        borderStyle = {border: '2px solid #039c00'}
      } else {
        borderStyle = {border: '3px solid #0081a8'}
      }
      return borderStyle
    },
  },

  methods: {
    ...mapActions("tagger", [
      "updateAnnotation",
      "deleteAnnotation",
    ]),
    updateAnnot(label) {
      this.updateAnnotation({
        labelId: label.id,
        annotationId: this.chunk.id
      })
    },
  }
}
</script>

<style scoped>
.highlight.blue {
  background: #edf4fa !important;
}

.highlight.bottom {
  display: inline-block;
  white-space: normal;
}

.highlight:first-child {
  margin-left: 0;
}

.highlight {
  /* border: 2px solid rgb(207, 216, 220); */
  margin: 4px 6px 4px 3px;
  vertical-align: middle;
  box-shadow: 2px 4px 5px rgba(0, 0, 0, .1);
  position: relative;
  cursor: default;
  min-width: 26px;
  line-height: 22px;
  display: flex;
}

.highlight .delete {
  top: -15px;
  left: -13px;
  /* top: -10px;
  left: -9px; */
  position: absolute;
  display: none;
  cursor: pointer
}

.highlight .link {
  top: -15px;
  right: -13px;
  /* top: -10px;
  right: -9px; */
  position: absolute;
  display: none;
  cursor: pointer
}

.highlight:hover .delete {
  display: block;
}

.highlight:hover .link {
  display: block;
}

.highlight .choose-target {
  display: none;
  position: absolute;
  top: -12px;
  right: -11px;
  width: 20px;
  background: rgba(0, 0, 0, 0.54);
  color: #ffffff;
  border-radius: 30px;
  cursor: pointer;
  text-align: center;
}

.highlight:hover .choose-target {
  display: block;
}

.highlight__content {
  display: flex;
  flex-wrap: wrap;
  align-items: center;
  padding: 2px 2px 0 6px;
  background: #ffffff;
}

.highlight.bottom .highlight__content:after {
  content: " ";
  padding-right: 3px;
}

.highlight__label {
  line-height: 14px;
  align-items: center;
  justify-content: center;
  display: flex;
  padding: 0 8px;
  text-align: center;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  color: white;
}

.highlight__label::after {
  content: attr(data-label);
  display: block;
  font-size: 12px;
  -webkit-font-smoothing: subpixel-antialiased;
  letter-spacing: .1em;
/* overwrites idealColor*/
  color: rgb(255, 255, 255); 
}

.highlight__rest-labels {
  line-height: 10px;
  align-items: center;
  justify-content: center;
  display: flex;
  padding: 0 6px;
  text-align: center;
  -webkit-user-select: none;
  -moz-user-select: none;
  -ms-user-select: none;
  user-select: none;
  color: white;
  box-shadow: 1px 2px 2px rgba(0, 0, 0, .0);
}

.highlight__rest-labels::after {
  content: attr(data-label);
  display: block;
  font-size: 9px;
  -webkit-font-smoothing: subpixel-antialiased;
  letter-spacing: .1em;
/* overwrites idealColor*/
  color: rgb(255, 255, 255); 
}

.newline {
  width: 100%;
}
</style>