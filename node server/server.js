const express = require("express");
const http = require("http");
const app = express();
const fs = require('fs');
var jsdom = require("jsdom/lib/old-api.js");
const { JSDOM } = jsdom;
var $ = require('jquery');
var path = require("path");
require("./assistiveJS.js");

app.listen(3000, function(){
  console.log('Listening on 3000')
});

app.get('/', function(req, res){
  res.sendFile(__dirname + '/index.html');
});

app.post('/submitted', function(req, res) {
    console.log('file sumbmitted');
    callServerCode();
});

function callServerCode() {

  var htmlSource = fs.readFileSync(__dirname + "/index.html", "utf8");
  call_jsdom(htmlSource, function (window) {
      var $ = window.$;
      var text = $("myForm.myFile.value");
      console.log(text);
      processTxt();
      $.getElementById('output').value = $(document).getElementById('myForm').myFile.value;
      $.getElementById('myForm').style.display = 'none';

      console.log(documentToSource(window.document));
  });


};

function processTxt(text){

  var data = { "essay": "hello world" };

  var post_options = {
      host: 'http://10.33.0.188',
      port: '8080',
      path: '/extendedEssay/compute',
      method: 'POST',
      payload: data,
      headers: {
          'Content-Type': 'application/JSON',
          'Content-Length': Buffer.byteLength(post_data)
      }
  };

  var post_req = http.request(post_options, function(res) {
        res.setEncoding('utf8');
        res.on('data', function (chunk) {
            console.log('Response: ' + chunk);
        });
    });

    // post the data
    post_req.write(post_data);
    post_req.end();

  executePost(text);

}

function call_jsdom(source, callback) {
    jsdom.env(source, [ 'jquery-1.7.1.min.js' ],
        function(errors, window) {
            process.nextTick(
                function () {
                    if (errors) {
                        throw new Error("There were errors: "+errors);
                    }
                    callback(window);
                }
            );
        }
    );
}
