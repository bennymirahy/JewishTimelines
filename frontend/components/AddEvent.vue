<template>
  <v-layout justify-center align-center>
    <template v-if="!loading">
      <v-form>
        <v-text-field v-model="event.description" label="Event peshat"></v-text-field>
        <v-text-field v-model="event.source" label="Source for the event"></v-text-field>
        <v-text-field v-model="event.age" type="number" label="Age"></v-text-field>
        <v-text-field v-model="event.sourceAge" label="Source for the age"></v-text-field>
      </v-form>
      <v-btn @click="save()" :loading="saving" color="accent">Submit</v-btn>
      <v-btn v-if="event.id" @click="remove()" :loading="removing" color="error" > Remove </v-btn>
  </template>
  </v-layout>
</template>

<script>

import Events from '~/components/Events.vue'
import AppApi from '~apijs'

export default {
  props: ['id'],
  data () {
    return {
      event: {
        age: 0,
        description: '',
        source: '',
        sourceAge: ''
      },
      loading: false,
      saving: false,
      removing: false
    }
  },
  created () {
    console.log('Event ID is:', this.id)
    if(this.id) {
      this.loading = true
      AppApi.get_event(this.id).then(response => {
        this.event = response.data
      })
      this.loading = false
    }
  },
  methods: {
    save(event) {
      this.saving = true
      AppApi.save_event(this.event).then(response => {
        this.$router.push({name: 'events'})
      })
      this.saving = false
    },
    remove(event) {
        this.removing = true
        AppApi.remove_event(this.event).then(response => {
          this.$router.push({name: 'events'})
        })
        this.removing = false
    }
  }
}

</script>

<style>
</style>
