var express = require('express');
var router = express.Router();

/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.get('/user/:name', function(req,res,next) {
  res.json({'url':'https://myanimeprofilepic.s3.amazonaws.com/'+req.params.name+'.png'});
});

module.exports = router;
