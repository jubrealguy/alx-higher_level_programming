#!/usr/bin/node

const arg = parseInt(process.argv.slice(2)[0], 10);

if (isNaN(arg)) {
  console.log('Not a number');
} else { console.log(`My number: ${arg}`); }
