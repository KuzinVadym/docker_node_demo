const express = require('express')
const app = express()

app.get('/', function (req, res) {
  res.json({message: 'Hello Test!'});
})

app.listen(3333, function () {
  console.log('Example app listening on port 3333!')
})