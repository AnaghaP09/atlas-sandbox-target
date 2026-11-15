# Demo sign-in page

A look-only page that shows what a company's own sign-in screen could look like in front of
ATLAS. Demo Corp is a made-up company.

The page does not sign anyone in. It has no password field, sends nothing and stores nothing.
Every button shows a short note that explains the real flow.

## Run it

```
python demo-sign-in/serve.py
```

Then open <http://127.0.0.1:8200>. Press Ctrl+C to stop. Use `--port` to pick another port.

The server answers only on this computer, serves only the files in this folder, and refuses any
request other than GET and HEAD.
