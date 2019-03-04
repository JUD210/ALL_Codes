// https://enyobook.wordpress.com/2016/08/17/export-default%EC%97%90-%EB%8C%80%ED%95%B4/

/*--------------------------------------------------------*/
// Named Exports
/*--------------------------------------------------------*/

//--- lib.js ---
export const sqrt = Math.sqrt
export function square(x) {
  return x * x
}
export function diag(x, y) {
  return sqrt(square(x) + square(y))
}

//--- main.js ---
import { square, diag } from "lib"
console.log(square(11)) // 121
console.log(diag(4, 3)) // 5

//---------------------------------

//--- main.js ---
import * as lib from "lib"
console.log(lib.square(11)) // 121
console.log(lib.diag(4, 3)) // 5

/*--------------------------------------------------------*/
// Default Exports
/*--------------------------------------------------------*/

//--- myFunc.js ---
export default function () {"..."};

//--- main1.js ---
import myFunc from 'myFunc';
myFunc();

//--- MyClass.js ---
export default class {"..."}

//--- main2.js ---
import MyClass from 'MyClass';
let inst = new MyClass();

//---------------------------------

//------ underscore.js ------
export default function(obj) {
  "..."
}
export function each(obj, iterator, context) {
  "..."
}
export { each as forEach }

//------ main.js ------
import _, { each } from "underscore"
