<template>
  <div id="connections-wrapper">
    <div class="highlight-container highlight-container--bottom-labels" @click="open" @touchend="open">
      <AnnotationItem
          v-for="(chunk, i) in chunks"
          :key="i"
          :chunk="chunk"
      />
      <v-menu
          v-model="showMenu"
          :position-x="x"
          :position-y="y"
          absolute
          offset-y
      >
        <v-list
            dense
            min-width="150"
            max-height="400"
            class="overflow-y-auto"
        >
          <v-list-item
              v-for="(label, i) in runLabels"
              :key="i"
              v-shortkey="[label.suffixKey]"
              @shortkey="assignLabel(label.id)"
              @click="assignLabel(label.id)"
          >
            <v-list-item-content>
              <v-list-item-title v-text="label.text"/>
            </v-list-item-content>
            <v-list-item-action>
              <v-list-item-action-text v-text="label.suffixKey"/>
            </v-list-item-action>
          </v-list-item>
        </v-list>
      </v-menu>
    </div>
  </div>
</template>

<script>
import {mapState, mapGetters, mapActions} from 'vuex';

import AnnotationItem from '@/components/tagging/AnnotationItem'

export default {
  components: {
    AnnotationItem
  },

  data() { 
    return {
      showMenu: false,
      x: 0,
      y: 0,
      start: 0,
      end: 0
    }
  },

  computed: {
    ...mapState("tagger", [
      "labels",
      "annotations",
    ]),
    ...mapGetters('tagger', [
      'docText',
      'runLabels',
      'sortAnnotations',
      'labelObject',
    ]),
    chunks() {
      let chunks = []
      let startOffset = 0
      // to count the number of characters correctly.
      const characters = [...this.docText]
      for (const annotation of this.sortAnnotations) {
        const label = this.labelObject[annotation.label]
        
        // add non-annotations to chunks.
        let piece = characters.slice(startOffset, annotation.startOffset).join('')
        chunks = chunks.concat(this.makeChunks(piece))
        startOffset = annotation.endOffset
        // add annotations to chunks.
        piece = characters.slice(annotation.startOffset, annotation.endOffset).join('')
        
        chunks.push({
          id: annotation.id,
          label: label.text,
          color: label.backgroundColor,
          text: piece,
          confidence: annotation.confidence,
          annotatedby: annotation.annotatedby,
        })
      }
      // add the rest of text.
      chunks = chunks.concat(this.makeChunks(characters.slice(startOffset, characters.length).join('')));
      return chunks;
    },
  },
  methods: {
    ...mapActions("tagger", [
      "addAnnotation",
    ]),
    makeChunks(text) {
      const chunks = []
      const snippets = text.split('\n')
      for (const snippet of snippets.slice(0, -1)) {
        chunks.push({
          label: null,
          annotatedby: null,
          color: null,
          text: snippet + '\n',
          newline: false,
        })
        chunks.push({
          label: null,
          annotatedby: null,
          color: null,
          text: '',
          newline: true,
        })
      }
      chunks.push({
        label: null,
        annotatedby: null,
        color: null,
        text: snippets.slice(-1)[0],
        newline: false
      })
      return chunks
    },

    show(e) {
      e.preventDefault()
      this.showMenu = false
      this.x = e.clientX || e.changedTouches[0].clientX
      this.y = e.clientY || e.changedTouches[0].clientY
      this.$nextTick(() => {
        this.showMenu = true
      })
    },

    setSpanInfo() {
      let selection
      // Modern browsers.
      if (window.getSelection) {
        selection = window.getSelection()
      } else if (document.selection) {
        selection = document.selection
      }
      // If nothing is selected.
      if (selection.rangeCount <= 0) {
        return
      }
      const range = selection.getRangeAt(0)
      const preSelectionRange = range.cloneRange()
      preSelectionRange.selectNodeContents(this.$el)

      preSelectionRange.setEnd(range.startContainer, range.startOffset)
      this.start = [...preSelectionRange.toString()].length
      this.end = this.start + [...range.toString()].length
    },

    validateSpan() {
      if ((typeof this.start === 'undefined') || (typeof this.end === 'undefined')) {
        return false
      }
      if (this.start === this.end) {
        return false
      }
      for (const annotation of this.annotations) {
        if ((annotation.startOffset <= this.start) && (this.start < annotation.endOffset)) {
          return false
        }
        if ((annotation.startOffset < this.end) && (this.end <= annotation.endOffset)) {
          return false
        }
        if ((this.start < annotation.startOffset) && (annotation.endOffset < this.end)) {
          return false
        }
      }
      return true
    },

    open(e) {
      this.setSpanInfo()
      if (this.validateSpan()) {
        this.show(e)
      }
    },
    assignLabel(labelId) {
      if (this.validateSpan()) {
        const payload = {
          startOffset: this.start,
          endOffset: this.end,
          labelId: labelId
        }
        this.addAnnotation(payload)
        this.showMenu = false
        this.start = 0
        this.end = 0
      }
    },

    drawnCountPoints(size) {
      const points = Array(size);

      for (let i = 0; i < points.length; i++) {
        points[i] = {
          drawn: 0,
          count: 0
        }
      }

      return points;
    }
  }
}
</script>

<style scoped>
.highlight-container.highlight-container--bottom-labels {
  align-items: flex-start;
}

.highlight-container {
  line-height: 40px !important;
  /* display: inline-flex;
  flex-wrap: wrap; */
  white-space: pre-wrap;
  cursor: default;
  position: relative;
  z-index: 1;
}

.highlight-container.highlight-container--bottom-labels .highlight.bottom {
  margin-top: 6px;
}

#connections-wrapper {
  position: relative;
}

#connections-wrapper canvas {
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  z-index: 0;
}
</style>