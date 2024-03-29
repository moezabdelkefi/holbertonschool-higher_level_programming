#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = `https://swapi-api.hbtn.io/api/films/${id}/`;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }

  if (response.statusCode !== 200) {
    console.error(`Request failed with status code ${response.statusCode}`);
    return;
  }

  const movie = JSON.parse(body);
  console.log(movie.title);
});
