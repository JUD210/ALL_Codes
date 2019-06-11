<template>
  <div>
    <h1>Events for {{ user.user.name }}</h1>
    <EventCard v-for="event in event.events" :key="event.id" :event="event" />

    <template v-if="page != 1">
      <router-link
        :to="{ name: 'event-list', query: { page: page - 1 } }"
        rel="prev"
        >Prev Page</router-link
      >
    </template>

    <template v-if="page != 1 && !isLastPage">
      |
    </template>

    <template v-if="!isLastPage">
      <router-link
        :to="{ name: 'event-list', query: { page: page + 1 } }"
        rel="next"
        >Next Page</router-link
      >
    </template>
  </div>
</template>

<script>
import EventCard from "@/components/EventCard.vue";
import { mapState } from "vuex";

export default {
  components: {
    EventCard
  },

  computed: {
    page() {
      return parseInt(this.$route.query.page) || 1;
    },
    isLastPage() {
      return this.event.eventsTotal <= this.page * 3;
    },
    ...mapState(["event", "user"])
  },

  created() {
    this.$store.dispatch("event/fetchEvents", {
      perPage: 3,
      page: this.page
    });
  }
};
</script>
