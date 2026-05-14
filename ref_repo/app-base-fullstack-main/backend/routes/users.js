var express = require('express');
var router = express.Router();
var userModel = require('../models/user.model');


/* GET users listing. */
router.get('/', function(req, res, next) {
  userModel.getUsers(req, res);
});

/* GET user by ID */
router.get('/:id', function(req, res, next) {
  userModel.getUserById(req, res);
});

/* Post user */
router.post('/', function(req, res, next) {
  userModel.createUser(req, res);
});

module.exports = router;
