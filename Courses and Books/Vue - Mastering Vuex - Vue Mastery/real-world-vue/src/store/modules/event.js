import EventService from "@/services/EventService.js";

export const namespaced = true;

export const state = {
  event: {},
  events: [],
  eventsTotal: 0
  // todos: [
  //   { id: 1, text: "...", done: true },
  //   { id: 2, text: "...", done: false },
  //   { id: 3, text: "...", done: true },
  //   { id: 4, text: "...", done: false }
  // ]
};

export const mutations = {
  ADD_EVENT(state, event) {
    state.events.push(event);
  },
  SET_EVENT(state, event) {
    state.event = event;
  },
  SET_EVENTS(state, events) {
    state.events = events;
  },
  SET_EVENTS_TOTAL(state, eventsTotal) {
    state.eventsTotal = eventsTotal;
  }
};

export const actions = {
  createEvent({ commit, rootState, dispatch }, event) {
    // Actions, Mutations, and Getters are always registered under the global namespace (aka. the root which is $store) even when using Modules.
    // No matter where they're declared, they're called without their module name.
    /* dispatch ('actionToCall') */

    // Calling actions inside another NameSpaced Module
    /* dispatch("moduleName/actionToCall", payload (ex: null), { root: true }) */

    console.log(`User creating Event is ${rootState.user.user.name}`);

    // NEVER call mutations in other modules, and
    // ONLY allow mutations to be called by actions in the same module.
    return EventService.postEvent(event)
      .then(() => {
        commit("ADD_EVENT", event);
        const notification = {
          type: "success",
          message: "Your event has been created!"
        };
        dispatch("notification/add", notification, { root: true });
      })
      .catch(error => {
        const notification = {
          type: "error",
          message: `There was a problem creating your event: ${error.message}`
        };
        dispatch("notification/add", notification, { root: true });
        throw error;
      });
  },

  // The payload in both Actions and Mutations can be a single variable OR an object.
  fetchEvent({ commit, getters, dispatch }, id) {
    var event = getters.getEventById(id);

    if (event) {
      commit("SET_EVENT", event);
    } else {
      EventService.getEvent(id)
        .then(response => {
          commit("SET_EVENT", response.data);
        })
        .catch(error => {
          const notification = {
            type: "error",
            message: `There was a problem fetching an event: ${error.message}`
          };
          dispatch("notification/add", notification, { root: true });
        });
    }
  },

  fetchEvents({ commit, dispatch }, { perPage, page }) {
    EventService.getEvents(perPage, page)
      .then(response => {
        commit("SET_EVENTS", response.data);
        commit("SET_EVENTS_TOTAL", response.headers["x-total-count"]);
      })
      .catch(error => {
        const notification = {
          type: "error",
          message: `There was a problem fetching events: ${error.message}`
        };
        dispatch("notification/add", notification, { root: true });
      });
  }
};

export const getters = {
  getEventById: state => id => {
    return state.events.find(event => event.id === id);
  }
  //
  // doneTodos: state => {
  //   return state.todos.filter(todo => todo.done);
  // },
  //
  // activeTodosCount: (state, getters) => {
  //   return state.todos.length - getters.doneTodos.length;
  //   or
  //   return state.todos.filter(todo => !todo.done).length;
  // }
};
