# Copilot / AI agent instructions for Basic Python Server

This repository is a minimal single-file Python HTTP server. The instructions below are concise, actionable, and focused on patterns discoverable in the codebase so an AI coding agent can be productive immediately.

## Big picture
- **Purpose:** A tiny local HTTP server that serves a static HTML page from `server.py` using Python's `http.server`.
- **Architecture:** Single-process, synchronous server. `HTTPServer` + `BaseHTTPRequestHandler` implementation in `server.py`.
- **Why this structure:** Simplicity — the project intentionally uses Python's standard library without frameworks or external deps.

## Key files
- `server.py`: entire application. Look here for request handling, default port, and the HTML payload (`HTML_PAGE`).

## How to run (developer workflows)
- Start locally: `python server.py` (defaults to port `8000`).
- Run on a different port from the command line:
  - Python one-liner: `python -c "from server import run_server; run_server(8080)"`
- Quick check from PowerShell: `Invoke-WebRequest http://localhost:8000` or `curl http://localhost:8000/`

## Code patterns & conventions (project-specific)
- Single-file app: add small features inside `server.py` unless you need to split for tests or complexity.
- Handler structure: extend `BaseHTTPRequestHandler` and implement `do_GET` for GET requests.
  - Logging: `log_message` is overridden to disable default logging. Use explicit `print()` calls for minimal logs (as used in `do_GET`).
- Static response: `HTML_PAGE` is a module-level multi-line string; modify it directly to change served content.
- Blocking behaviour: `server.serve_forever()` is blocking — any long-running request will block other connections.

## Integration points & caveats
- No external dependencies or config files are present. Changes that add dependencies should also add `requirements.txt`.
- No tests are present. If adding tests, prefer `pytest` and split logic into importable functions to avoid starting the server on import.
- If you add an environment/config layer, prefer explicit parameters on `run_server(port)` rather than implicit globals.

## Debugging notes
- To see request logs: `print()` is used in `do_GET` (prints client address). Avoid re-enabling `BaseHTTPRequestHandler.log_message` unless you want per-request logging to stderr.
- To stop the server, use Ctrl+C in the terminal running `python server.py`.

## Example edits an AI agent might be asked to make (and how to do them)
- Change default port: update `run_server(port=8000)` signature and the `if __name__ == "__main__"` call.
- Serve JSON on `/api`: in `do_GET`, inspect `self.path` and set `Content-Type: application/json` and write `bytes(json.dumps(obj), 'utf-8')`.
- Add graceful shutdown: replace `serve_forever()` with `try/except KeyboardInterrupt` around the loop and call `server.server_close()` on exit.

## PR/Commit guidance for AI agents
- Keep changes minimal and focused — this repo is intentionally tiny.
- If adding new files (tests, deps), update repository root with `requirements.txt` and a short `README.md` describing run steps.

If anything here is unclear or you want additional examples (tests, JSON API, or concurrency), tell me which area to expand.
