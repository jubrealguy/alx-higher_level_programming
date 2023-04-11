#!/usr/bin/node

(function add (a, b) {
  a = Number(process.argv.slice(2)[0]);
  b = Number(process.argv.slice(2)[1]);

  console.log(a + b);
})();
