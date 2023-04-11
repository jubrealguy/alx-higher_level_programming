#!/usr/bin/node

const arg = Number(process.argv.slice(2)[0]);

function factorial (n) {
  if (n === 0 || isNaN(n)) {
    return 1;
  } else { return n * factorial(n - 1); }
}
console.log(factorial(arg));
