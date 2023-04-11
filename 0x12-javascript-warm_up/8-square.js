#!/usr/bin/node

const arg = process.argv.slice(2)[0];

if (isNaN(arg)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < arg; i++) {
    console.log('X'.repeat(arg));
  }
}
