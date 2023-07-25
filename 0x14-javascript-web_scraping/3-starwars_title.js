#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/films/';
const moveId = process.argv[2];

request.get(url + moveId, (err, res, body) => {
  if (err) { console.log(err); } else if (res.statusCode === 200) {
    const resJSON = JSON.parse(body);
    console.log(resJSON.title);
  } else {
    console.log(`Error code: ${res.statusCode}`);
  }
});
