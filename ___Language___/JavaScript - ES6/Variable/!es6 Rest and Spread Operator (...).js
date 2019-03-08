function myFunc1(...[x, y, z]) {
  return x * y * z
}

console.log(myFunc1(1)) // NaN
console.log(myFunc1(1, 2, 3)) // 6
console.log(myFunc1(1, 2, 3, 4)) // 6 (fourth parameter is not destructured)

/*--------------------------------------------------------*/

function myFunc2(x, y, ...params) {
  // used rest operator here
  console.log(x) // a
  console.log(y) // b
  console.log(params) // ['c', 'd', 'e', 'f']
}

var inputs = ["a", "b", "c", "d", "e", "f"]
myFunc2(...inputs) // used spread operator here
// "a"
// "b"
// ["c", "d", "e", "f"]

/*--------------------------------------------------------*/

const featured = ["Deep Dish", "Pepperoni", "Hawaiian"]
const specialty = ["Meatzza", "Spicy Mama", "Margherita"]

const pizzas = [...featured, "veg pizza", ...specialty]

console.log(pizzas) // ['Deep Dish', 'Pepperoni', 'Hawaiian', 'veg pizza', 'Meatzza', 'Spicy Mama', 'Margherita']

/*--------------------------------------------------------*/

var obj1 = { foo: "bar", x: 42 }
var obj2 = { foo: "baz", y: 13 }

var clonedObj = { ...obj1 }
console.log(clonedObj);
// { foo: "bar", x: 42 }

var mergedObj = { ...obj1, ...obj2 }
console.log(mergedObj);
// { foo: "baz", x: 42, y: 13 }
