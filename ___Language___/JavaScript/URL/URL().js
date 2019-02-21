var a = new URL("/", "https://developer.mozilla.org");
// Creates a URL pointing to 'https://developer.mozilla.org/'

var b = new URL("https://developer.mozilla.org");
// Creates a URL pointing to 'https://developer.mozilla.org/'

var c = new URL("en-US/docs", b);
// Creates a URL pointing to 'https://developer.mozilla.org/en-US/docs'

var d = new URL("/en-US/docs", b);
// Creates a URL pointing to 'https://developer.mozilla.org/en-US/docs'

var f = new URL("/en-US/docs", d);
// Creates a URL pointing to 'https://developer.mozilla.org/en-US/docs'

var g = new URL("/en-US/docs", "https://developer.mozilla.org/fr-FR/toto");
// Creates a URL pointing to 'https://developer.mozilla.org/en-US/docs'
var h = new URL("/en-US/docs", a);
// Creates a URL pointing to 'https://developer.mozilla.org/en-US/docs'

var i = new URL("/en-US/docs", "");
// Raises a TypeError exception as '' is not a valid URL

var j = new URL("/en-US/docs");
// Raises a TypeError exception as '/en-US/docs' is not a valid URL

var k = new URL("http://www.example.com", "https://developers.mozilla.com");
// Creates a URL pointing to 'http://www.example.com/'

var l = new URL("http://www.example.com", b);
// Creates a URL pointing to 'http://www.example.com/'
