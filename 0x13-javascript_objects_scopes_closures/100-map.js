#!/usr/bin/node

const aList = require('./100-data').list;

const newList = aList.map((item, index) => { return item * aList.indexOf(item); });

console.log(aList);
console.log(newList);
