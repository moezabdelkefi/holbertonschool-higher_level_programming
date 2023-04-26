#!/usr/bin/node
const request = require('request');

const url = process.argv[2];

request(url, function (error, response, body) {
  if (error) {
    console.error(error);
    return;
  }

  const films = JSON.parse(body).results;
  let count = 0;

  for (const film of films) {
    const characters = film.characters;
    if (characters.indexOf('https://swapi-api.hbtn.io/api/people/18/') !== -1) {
      count++;
    }
  }

  console.log(count);
});
