var express = require('express');
var router = express.Router();
var fs = require('fs');
var crypto = require('crypto');
var exec = require('child_process').spawn;
const out = fs.openSync('./out.log', 'a');
const err = fs.openSync('./out.log', 'a');
/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.post('/user', function(req,res,next) {
  console.log(req.files);
  var face = req.files.face;
  face.mv('faces/'+crypto.createHash('md5').update(req.body.name+"face").digest("hex")+".png", function(err) {
    exec("sh", ['run.sh',req.body.name],{ detached: true, stdio:['ignore',out,err]});
    res.render('success',{url:'https://myanimeprofilepic.s3.amazonaws.com/'+req.body.name+'.png'});
  });
});

module.exports = router;
