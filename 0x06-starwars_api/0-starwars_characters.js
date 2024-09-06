#!/usr/bin/node

const request = require('request');

const number = process.argv[2];
request(
  `https://swapi-api.alx-tools.com/api/films/${number}/`, (error, body) => {
    if (error) { console.log(error); }
    const newbody = JSON.parse(body.body);
    const chars = newbody.characters;

    const characterPromises = chars.map(link => {
      return new Promise((resolve, reject) => {
        request(link, (error, body) => {
          if (error) { reject(error); }
          const charcter = JSON.parse(body.body);
          resolve(charcter.name);
        });
      });
    });

    Promise.all(characterPromises)
      .then(names => {
        names.forEach(namer => console.log(namer));
      })
      .catch(error => console.log(error));
  }
);
