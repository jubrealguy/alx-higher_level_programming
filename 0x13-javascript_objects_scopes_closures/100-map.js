#!/usr/bin/node

const aList = require('./100-data').list;
console.log(aList);

const newList = aList.map((item) => { return item * aList.indexOf(item); });
console.log(newList);
