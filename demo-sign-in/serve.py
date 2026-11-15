"""Serve the demo sign-in page on this computer only.

Usage:  python demo-sign-in/serve.py            (http://127.0.0.1:8200)
        python demo-sign-in/serve.py --port 8201

The page is a look-only demo. It accepts only GET and HEAD, serves only the three files in this
folder, and loads nothing from other sites.
"""

import argparse
import http.server
from pathlib import Path

HERE = Path(__file__).resolve().parent
FILES = {
    "/": ("index.html", "text/html; charset=utf-8"),
    "/index.html": ("index.html", "text/html; charset=utf-8"),
    "/style.css": ("style.css", "text/css; charset=utf-8"),
    "/app.js": ("app.js", "text/javascript; charset=utf-8"),
}
HEADERS = {
    "Content-Security-Policy": (
        "default-src 'none'; style-src 'self'; script-src 'self'; img-src 'self' data:; "
        "form-action 'none'; frame-ancestors 'none'; base-uri 'none'"
    ),
    "X-Content-Type-Options": "nosniff",
    "Referrer-Policy": "no-referrer",
    "Cache-Control": "no-store",
}


class Handler(http.server.BaseHTTPRequestHandler):
    server_version = "demo"
    sys_version = ""

    def _send(self, include_body: bool) -> None:
        entry = FILES.get(self.path.split("?", 1)[0])
        if entry is None:
            self.send_error(404, "Not found")
            return
        name, kind = entry
        body = (HERE / name).read_bytes()
        self.send_response(200)
        self.send_header("Content-Type", kind)
        self.send_header("Content-Length", str(len(body)))
        for key, value in HEADERS.items():
            self.send_header(key, value)
        self.end_headers()
        if include_body:
            self.wfile.write(body)

    def do_GET(self) -> None:  # noqa: N802
        self._send(include_body=True)

    def do_HEAD(self) -> None:  # noqa: N802
        self._send(include_body=False)

    def _refuse(self) -> None:
        self.send_error(405, "Demo page: only GET and HEAD")

    do_POST = do_PUT = do_PATCH = do_DELETE = _refuse  # noqa: N815


def main() -> None:
    parser = argparse.ArgumentParser(description="Serve the demo sign-in page on 127.0.0.1.")
    parser.add_argument("--port", type=int, default=8200)
    args = parser.parse_args()
    server = http.server.ThreadingHTTPServer(("127.0.0.1", args.port), Handler)
    print(f"Demo sign-in page: http://127.0.0.1:{args.port}/  (press Ctrl+C to stop)")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        server.server_close()


if __name__ == "__main__":
    main()
