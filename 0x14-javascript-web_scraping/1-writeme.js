#!/usr/bin/node
const fs = require('fs')
const file_path = process.argv[2];
const content = process.argv[3];

fs.writeFile(file_path, content, 'utf-8', (err) => {
	if (err) console.log(err);
});
