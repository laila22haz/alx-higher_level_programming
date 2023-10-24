#!/usr/bin/node

const request = require('request');
const id = process.argv[2];

function getTitle (episode) {
  const url = `https://swapi-api.alx-tools.com/api/films/${episode}`;
  request(url, (error, response, body) => {
    if (!error) {
      const data = JSON.parse(body);
      const title = data.title;
      console.log(title);
    } else {
      console.error(error);
    }
  });
}

const episode = id;
if (episode) {
  getTitle(episode);
}
