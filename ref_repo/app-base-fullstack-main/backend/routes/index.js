var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.send({ api: 'Bem-vindo(a) a minha API com Node e Express' });
});

module.exports = router;
