let app = new Vue({
  el: "#app",
  data: {
    product: "Socks",

    inventory: 9,

    details: ["80% cotton", "20% polyester", "ender-neutral"],
    variants: [
      {
        id: 2234,
        color: "green",
        size: ["S", "M", "L"]
      },
      {
        id: 2235,
        color: "blue",
        size: ["S", "M", "L"]
      }
    ],

    description: "It's very comfortable!",

    image: "./assets/vmSocks-green-onWhite.jpg"
  }
});
