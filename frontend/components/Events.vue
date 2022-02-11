<template>
  <v-layout justify-center align-center>

  <v-timeline light>
    <v-timeline-item
      v-for="event in events"
      :key="event.description"
      color="yellow darken-3"
      dark
      small
    >
      <template v-slot:opposite>
        <v-tooltip v-if="event.sourceAge" bottom close-delay="500">
          <template v-slot:activator="{ on }">
            <v-chip v-on="on">
              Age: {{ event.age }}
            </v-chip>
          </template>
          <span> {{ event.sourceAge }} </span>
        </v-tooltip>
      </template>
      <v-card class="elevation-2-event">
        <v-card-title class="font-weight-medium"> {{ event.description }} </v-card-title>
        <v-card-text class="font-weight-thin"> {{ event.source }} </v-card-text>
        <v-card-text> 
          <v-btn
            :to="{name: 'update-event-id', params: {id: event.id}} " >Edit this event
          </v-btn>
        </v-card-text>
      </v-card>
    </v-timeline-item>
  </v-timeline>

  <v-btn :to="{name: 'update-event-id'}">Add new event</v-btn>

  </v-layout>
</template>

<script>

import AppApi from '~apijs'

export default {
  data () {
    return {
      events: []
    }
  },
  created() {
    AppApi.list_events().then(response => {
      this.events = response.data
      
    })
    console.log('Events listed')
    console.log(this.events)
  },
}
</script>

<style>
</style>
