
Executable File·5 lines (5 loc) · 160 Bytes
#!/usr/bin/node
const req = require('request');
req.get(process.argv[2], (err, res) => {
  err ? console.log(err) : console.log('code: ' + res.statusCode);
});

