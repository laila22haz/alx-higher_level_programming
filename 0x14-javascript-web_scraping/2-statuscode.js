#!/usr/bin/node

const request = require('request');
const url = process.argv[2];

request(url, { json: true }, function (error, response, body) {
  if (error) {
    return console.error(error);
  } else {
    console.log('code:', response.statusCode);
  }
});
