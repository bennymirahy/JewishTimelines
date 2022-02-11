<template>
  <v-layout justify-center align-center>

    <AddEvent :id="$route.params.id"></AddEvent>
    
  </v-layout>
</template>

<script>

import AddEvent from '~/components/AddEvent.vue'

export default {
  data () {
    return {}
  },
  components: {
    AddEvent
  }
}
</script>

<style>
</style>
