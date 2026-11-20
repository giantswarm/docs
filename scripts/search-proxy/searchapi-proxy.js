// Local reverse proxy that makes the docs search widget work in `make dev`.
//
// The widget calls /searchapi, which only exists on the docs-proxy in
// production. This proxy serves everything from one local origin: it forwards
// /searchapi to the upstream docs site and passes every other request through
// to the local Hugo server, so the browser only ever talks to one origin and
// there is no CORS problem. WebSocket upgrades are passed through too, so
// Hugo's livereload keeps working.
//
// `make dev` starts this automatically. Open http://localhost:8888.
//
// Environment:
//   SEARCH_PROXY_PORT   port to listen on            (default 8888)
//   HUGO_PORT           local Hugo server port       (default 1313)
//   SEARCHAPI_UPSTREAM  origin that serves /searchapi (default https://docs.giantswarm.io)
//
// Node built-in modules only, so there is nothing to install.
const http = require("http");
const https = require("https");
const net = require("net");
const { URL } = require("url");

const PORT = Number(process.env.SEARCH_PROXY_PORT) || 8888;
const HUGO_PORT = Number(process.env.HUGO_PORT) || 1313;
const UPSTREAM = new URL(process.env.SEARCHAPI_UPSTREAM || "https://docs.giantswarm.io");
const UPSTREAM_HOST = UPSTREAM.hostname;
const UPSTREAM_PORT = Number(UPSTREAM.port) || (UPSTREAM.protocol === "http:" ? 80 : 443);
const UPSTREAM_HTTP = UPSTREAM.protocol === "http:" ? http : https;

const server = http.createServer(function (req, res) {
  if (req.url.indexOf("/searchapi") === 0) {
    const upstream = UPSTREAM_HTTP.request(
      {
        host: UPSTREAM_HOST,
        port: UPSTREAM_PORT,
        path: req.url,
        method: req.method,
        headers: Object.assign({}, req.headers, { host: UPSTREAM_HOST }),
      },
      function (r) {
        res.writeHead(r.statusCode, r.headers);
        r.pipe(res);
      }
    );
    upstream.on("error", function (e) {
      res.writeHead(502);
      res.end("searchapi proxy error: " + e.message);
    });
    req.pipe(upstream);
    return;
  }

  const upstream = http.request(
    {
      host: "localhost",
      port: HUGO_PORT,
      path: req.url,
      method: req.method,
      headers: Object.assign({}, req.headers, { host: "localhost:" + HUGO_PORT }),
    },
    function (r) {
      res.writeHead(r.statusCode, r.headers);
      r.pipe(res);
    }
  );
  upstream.on("error", function (e) {
    res.writeHead(502);
    res.end("hugo proxy error (is make dev running?): " + e.message);
  });
  req.pipe(upstream);
});

// Pass WebSocket upgrades through so Hugo livereload keeps working. Everything
// that upgrades is local, so it always goes to Hugo, never to the upstream.
server.on("upgrade", function (req, clientSocket, head) {
  const upstream = net.connect(HUGO_PORT, "localhost", function () {
    const headerLines = [req.method + " " + req.url + " HTTP/1.1"];
    for (let i = 0; i < req.rawHeaders.length; i += 2) {
      headerLines.push(req.rawHeaders[i] + ": " + req.rawHeaders[i + 1]);
    }
    upstream.write(headerLines.join("\r\n") + "\r\n\r\n");
    if (head && head.length) upstream.write(head);
    upstream.pipe(clientSocket);
    clientSocket.pipe(upstream);
  });
  upstream.on("error", function () {
    clientSocket.destroy();
  });
  clientSocket.on("error", function () {
    upstream.destroy();
  });
});

server.listen(PORT, function () {
  console.log(
    "Search dev proxy: open http://localhost:" + PORT +
      "  (site -> :" + HUGO_PORT + ", /searchapi -> " + UPSTREAM.origin + ")"
  );
});
