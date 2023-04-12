#!/usr/bin/node

const dict = require('./101-data').dict;

const list = Object.entries(dict);
const uniqValues = [...new Set(Object.values(dict))];
const newDict = {};
for (const i in uniqValues) {
  const newList = [];
  for (const j in list) {
    if (list[j][1] === uniqValues[i]) {
      newList.unshift(list[j][0]);
    }
  }
  newDict[uniqValues[i]] = newList;
}
console.log(newDict);
