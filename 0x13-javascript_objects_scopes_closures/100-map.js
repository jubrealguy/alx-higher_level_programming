#!/usr/bin/node

const aList = require('./100-data').list;
console.log(aList);

const newList = aList.map((item, index) => { return (item * index); });
console.log(newList);
