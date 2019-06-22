var eventBus = new Vue();

/*--------------------------------------------------------*/

Vue.component("product", {
  // props: [message],
  props: {
    premium: {
      type: Boolean,
      required: true
    }
  },

  template: /* html */ `
  <div class="product">
    <div class="product-image">
      <img :src="image" /><br />
      <a :href="image">click to enlarge</a>
    </div>

    <div class="product-info">
      <h1>{{ title }}</h1>


      <span v-if="inventory > 10">In Stock</span>
      <span v-else-if="inventory > 0">Almost sold out!</span>
      <span v-else :class="{'info--outOfStock': inventory <= 0}"
        >Out of Stock</span
      >
      <span v-show="inventory > 0">({{ inventory }} left.)</span>
      <p>{{sale}}</p>
      <p>Shipping: {{ shipping }}</p>

      <hr />

      <h2>Variants</h2>

      <p>Fabric</p>
      <product-details :details="details"></product-details>

      <p>Size</p>
      <ul>
        <li v-for="size in sizes">
          {{ size }}
        </li>
      </ul>

      <p>Color</p>

      <span
        class="color-box"
        :style="[styleObject_color_box, {backgroundColor: variant.color}]"
        v-for="(variant, index) in variants"
        :key="variant.id"
        @mouseover="updateProduct(index)"
      >&nbsp;{{ variant.id }}&nbsp;</span>

      <hr />

      <p>{{ description }}</p>

      <button
        @click="addToCart"
        :disabled="inventory <= 0"
        :class="[classObject_add_btn, inventory <= 0 ? 'btn--inactive' : 'btn--active']"
      >
        Add to Cart
      </button>
      <button @click="removeCart">Remove Cart</button>

    </div>

    <product-tabs :reviews="reviews"></product-tabs>


  </div>
`,

  data() {
    return {
      // for practice
      styleObject_color_box: {
        "font-size": "30px",
        color: "white"

        // Not works in span
        // width: "40px",
        // height: "40px",
        // "margin-top": "5px"
      },

      // for practice
      classObject_add_btn: {
        add_btn: true
      },

      // image: "./assets/vmSocks-green-onWhite.jpg",

      brand: "Hyeogikarp",
      product: "Socks",

      onSale: true,

      details: ["80% cotton", "20% polyester", "ender-neutral"],
      sizes: ["S", "M", "L"],

      selectedVariant: 0,

      variants: [
        {
          id: 2234,
          color: "green",
          image: "./assets/vmSocks-green-onWhite.jpg",
          quantity: 11
        },
        {
          id: 2235,
          color: "blue",
          image: "./assets/vmSocks-blue-onWhite.jpg",
          quantity: 7
        },
        {
          id: 2236,
          color: "red",
          image: "./assets/vmSocks-red-onWhite.jpg",
          quantity: 0
        }
      ],

      description: "It's very comfortable!",

      reviews: []
    };
  },

  methods: {
    addToCart: function() {
      this.$emit("add-to-cart", this.variants[this.selectedVariant].id);
    },
    removeCart() {
      this.$emit("remove-cart", this.variants[this.selectedVariant].id);
    },
    updateProduct(index) {
      this.selectedVariant = index;
    }
  },

  computed: {
    title() {
      return `${this.brand}'s ${this.product}`;
    },
    image() {
      return this.variants[this.selectedVariant].image;
    },
    inventory() {
      return this.variants[this.selectedVariant].quantity;
    },
    sale() {
      if (this.onSale) {
        return `It's on ?% sale!`;
      } else {
        return `It's not on sale!`;
      }
    },
    shipping() {
      if (this.premium) {
        return "Free";
      }
      return 2.99;
    }
  },

  mounted() {
    eventBus.$on("review-submitted", productReview => {
      this.reviews.push(productReview);
    });
  }
});

/*--------------------------------------------------------*/

Vue.component("product-details", {
  props: {
    details: {
      type: Array,
      required: true
    }
  },
  template: /* html */ `
      <ul class="product-details">
        <li v-for="detail in details">
          {{ detail }}
        </li>
      </ul>
  `
});

/*--------------------------------------------------------*/

Vue.component("product-tabs", {
  props: {
    reviews: {
      type: Array,
      required: true
    }
  },
  template: /* html */ `
  <div>
    <span class="tab"
          :class="{ activeTab: selectedTab === tab}"
          v-for="(tab, index) in tabs"
          :key="index"
          @click="selectedTab = tab"
    >{{ tab }}</span>

    <div class="product-reviews" v-show="selectedTab === 'Reviews'">
      <p v-if="!reviews.length"> There are no reviews yet. </p>
      <ul>
        <li v-for="review in reviews">
          <p>{{ review.name }}</p>
          <p>Rating: {{ review.rating }}/5</p>
          <p>Recommend:{{ review.recommend }}</p>
          <p>{{ review.review }}</p>
        </li>
      </ul>
    </div>


    <product-review v-show="selectedTab === 'Write a review'"
    ></product-review>

  </div>
  `,

  data() {
    return {
      tabs: ["Reviews", "Write a review"],
      selectedTab: "Reviews"
    };
  }
});

/*--------------------------------------------------------*/

Vue.component("product-review", {
  template: /* html */ `
  <form class="review-form" @submit.prevent="onSubmit">

    <p class="error" v-if="errors.length">
    <strong>Please correct the following error(s):</strong>
      <ul>
        <li v-for="error in errors">{{ error }}</li>
      </ul>
    </p>

    <p>
      <label for="name">Name:</label>
      <input id="name" v-model="name" />
    </p>

    <hr>

    <p>
      <label for="review">Review:</label>
      <textarea id="review" v-model="review"></textarea>
    </p>

    <hr>

    <p>
      <label for="rating">Rating:</label>
      <select id="rating" v-model.number="rating">
        <option>5</option>
        <option>4</option>
        <option>3</option>
        <option>2</option>
        <option>1</option>
      </select>
    </p>

    <hr>

    <p>Would you recommend this product?</p>

    <label>Yes</label>
    <input type="radio" value="Yes" v-model="recommend"/>
    <br>

    </label>No</label>
    <input type="radio" value="No" v-model="recommend"/>

    <hr>

    <p>
      <input type="submit" value="Submit">
    </p>
  </form>
  `,

  data() {
    return {
      name: null,
      review: null,
      rating: null,
      recommend: null,
      errors: []
    };
  },

  methods: {
    onSubmit() {
      this.errors = [];

      if (this.name && this.review && this.rating && this.recommend) {
        let productReview = {
          name: this.name,
          review: this.review,
          rating: this.rating,
          recommend: this.recommend
        };

        eventBus.$emit("review-submitted", productReview);

        this.name = null;
        this.review = null;
        this.rating = null;
        this.recommend = null;
      } else {
        if (!this.name) this.errors.push("Name is required.");
        if (!this.review) this.errors.push("Review is required.");
        if (!this.rating) this.errors.push("Rating is required.");
        if (!this.recommend) this.errors.push("Recommned is required.");
      }
    }
  }
});

/*--------------------------------------------------------*/

let app = new Vue({
  el: "#app",

  data: {
    premium: true,
    cart: []
  },

  methods: {
    addToCart(id) {
      this.cart.push(id);
    },

    removeCart(id) {
      for (i = this.cart.length - 1; i >= 0; i--) {
        if (this.cart[i] === id) {
          this.cart.splice(i, 1);
        }
      }
    }
  }
});
