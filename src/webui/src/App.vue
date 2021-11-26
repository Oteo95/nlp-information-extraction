<template>
  <v-app class="grey lighten-4">
    <Navbar />
      <v-main>
          <router-view :key="$route.path"></router-view>
      </v-main>
  </v-app>
</template>
<script>
import Navbar from './components/Navbar'

export default {
  name: 'App',
  components: {
    Navbar,
  },
  data: () => ({
    //
  }),
};
</script>