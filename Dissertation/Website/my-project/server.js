const http = require('http');

const hostname = '138.68.177.42';
const port = 3000;

const server = http.createServer((req, res) => {
	res.statusCode = 200;
  	res.setHeader('Content-Type', 'text/plain');
  	res.end('This is the Main App!\n');
});

server.listen(port, hostname, () => {
  	console.log(`Server running at http://${hostname}:${port}/`);
});
##adminside code
const http = require('http');

const hostname = '138.68.177.42';
const port = 3001;

const server = http.createServer((req, res) => {
	res.statusCode = 200;
  	res.setHeader('Content-Type', 'text/plain');
  	res.end('This is the Admin Side!\n');
});

server.listen(port, hostname, () => {
  	console.log(`Server running at http://${hostname}:${port}/`);
});
