var express = require('express');
var router = express.Router();
var crypto = require('crypto');
var exec = require('child_process').exec;
/* GET home page. */
router.get('/', function(req, res, next) {
  res.render('index', { title: 'Express' });
});

router.post('/user', function(req,res,next) {
  console.log(req.files);
  var face = req.files.face;
  face.mv('faces/'+crypto.createHash('md5').update(req.body.name+"face").digest("hex")+".png", function(err) {
    exec("python script.py "+req.body.name,function (error, stdout, stderr) {
      console.log(error + " " + stdout + " " +stderr);
      res.render('success',{url:'https://myanimeprofilepic.s3.amazonaws.com/'+req.body.name+'.png'});
    });
  });
});

module.exports = router;
