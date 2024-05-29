#!/usr/bin/node

const fs = require('fs');

function writeFile (filePath, content){
	fs.writeFile(filePath, content, 'utf-8', (err) =>{
		if (err){
			console.error(`An error has occured: ${err}`);
		}
	});
}

if (process.argv.length >3){
	const filePath = process.argv[2];
	const content = process.argv[3];
	writeFile(filePath, content);
}else{
	console.log('Please provide the file path.');
}
