<template>
  <v-container
      fluid
      fill-height
      class="pa-0 grey lighten-4"
  >
    <v-layout row wrap justify-space-around>
      <v-flex class="mt-5 mb-10" xs11 sm10 lg9 xl8>
        <DocTable />
      </v-flex>
    </v-layout>
  </v-container>
</template>

<script>
import DocTable from "@/components/tables/DocTable"

export default {
  name: 'DocTables',
  components: {
    DocTable,
  }
}
</script>
