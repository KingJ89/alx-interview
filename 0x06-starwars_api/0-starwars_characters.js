#!/usr/bin/node
// Script that prints all characters of a Star Wars movie.
const request = require('request');
const movieId = process.argv[2];
const apiUrl = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(apiUrl, { method: 'GET' }, (error, response, body) => {
  if (error) {
    console.error('Error fetching movie:', error);
    return;
  }

  try {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  } catch (parseError) {
    console.error('Error parsing response:', parseError);
  }
});

function printCharacters(characters, index) {
  if (index >= characters.length) return;

  request(characters[index], { method: 'GET' }, (error, response, body) => {
    if (error) {
      console.error('Error fetching character:', error);
      return;
    }

    try {
      const characterName = JSON.parse(body).name;
      console.log(characterName);
      printCharacters(characters, index + 1);
    } catch (parseError) {
      console.error('Error parsing character:', parseError);
    }
  });
}
