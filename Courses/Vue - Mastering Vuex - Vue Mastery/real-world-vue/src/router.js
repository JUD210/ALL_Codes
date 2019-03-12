import Vue from "vue";
import Router from "vue-router";

import EventList from "./views/EventList.vue";
import EventShow from "./views/EventShow.vue";
import EventCreate from "./views/EventCreate.vue";

Vue.use(Router);

export default new Router({
  mode: "history",
  routes: [
    {
      path: "/",
      name: "event-list",
      component: EventList
    },
    {
      path: "/event/:id",
      name: "event-show",
      component: EventShow,
      props: true
    },
    {
      path: "/event/create",
      name: "event-create",
      component: EventCreate
    }
  ]
});

/* 
If we care about SEO, we might not want to have two pages with the same content. but, it's good to know how to do this.

alias: "/evt-lst"
*/
