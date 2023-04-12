#!/usr/bin/node

const fs = require('fs');

const args = process.argv.slice(2);
const firstArg = args[0];
const secondArg = args[1];
const thirdArg = args[2];

const firstContent = fs.readFileSync(firstArg).toString();
const secondContent = fs.readFileSync(secondArg).toString();

fs.writeFileSync(thirdArg, firstContent + secondContent);
