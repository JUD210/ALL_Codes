var counter = 100

var t = 1.5
var activated = 0

newYearCountdown = setInterval(function() {
  console.log(counter)
  counter--
  if (counter === 0) {
    console.log("HAPPY NEW YEAR!!")
    clearInterval(newYearCountdown)
  }

  if (doit) {
    console.log(`IN! activated: `)
    console.log(JSON.stringify(activated))
    window.clearInterval(activated)
    activated = setInterval(() => {
      console.log(t * 1000)
    }, t * 1000)

    doit = false
  }
}, 1000)

// use console and manually imitate trigger
//
// doit=true
