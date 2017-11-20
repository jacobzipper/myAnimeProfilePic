var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/user/:name', function(req,res,next) {
  res.json({'url':'https://s3.amazonaws.com/myanimeprofilepic/'+req.params.name+'.png'});
});

module.exports = router;
