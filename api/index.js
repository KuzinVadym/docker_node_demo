import express from 'express';
import request from 'request';

import settings from './settings';
import database from './database';

let reqOptions = require('./helpers/reqOptions');

const mode = process.env['MODE'] || 'dev';
const app = express();
settings.set(mode);
database.init();

function getTestInfo() {
  return new Promise(function(resolve, reject) {
    let url = 'http://test:3333/';
    request(reqOptions(url), (error, response, test) => {
      if (error) reject(error);
      console.log(test);
      resolve(test);
    });
  });
}

app.get('/', function (req, res) {
  const db = database.get();
  db.collection('mongoclient_test').insert({name: 'Vadym', nachname: 'Kuzin', position: 'Senior FullStack Dev'})
  .then(result => {
    console.log(result);
    res.send(result.ops[0]);
  });
});

app.get('/test', function (req, res) {
  console.log("test");
  getTestInfo()
  .then(result => {
    console.log(result);
    res.send(result);
  });
});

app.listen(3000, function () {
  console.log('Example app listening on port 3000!')
});