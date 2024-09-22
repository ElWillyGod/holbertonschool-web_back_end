const http = require('http');

const port = 1245;

const server = (req, res) => {
  res.writeHead(200, { 'Content-Type': 'text/plain' });
  res.end('Hello Holberton School!');
};

const app = http.createServer(server);
app.listen(port, () => {
  console.log('...');
});

module.exports = app;
