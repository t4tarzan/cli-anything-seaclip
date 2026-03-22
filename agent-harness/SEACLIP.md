# CLI-Anything: SeaClip-Lite Harness

CLI harness for SeaClip-Lite project management board.

## Backend

- FastAPI at `http://127.0.0.1:5200`
- SQLite at `/Users/whitenoise-oc/shrirama/seaclip-lite/seaclip.db`

## Install

```bash
cd agent-harness
pip install -e .
```

## Usage

```bash
# Interactive REPL
cli-anything-seaclip

# One-shot commands
cli-anything-seaclip --json issue list
cli-anything-seaclip --json issue list --status backlog --priority high
cli-anything-seaclip --json issue create --title "Fix login bug" --priority high
cli-anything-seaclip --json agent list
cli-anything-seaclip --json pipeline start --issue UUID --mode auto
cli-anything-seaclip --json pipeline status --issue UUID
cli-anything-seaclip --json scheduler list
cli-anything-seaclip --json activity list --limit 20
cli-anything-seaclip --json server health
```

## Command Groups

| Group       | Commands                        |
|-------------|--------------------------------|
| `issue`     | list, create, move, status, delete |
| `agent`     | list                           |
| `pipeline`  | start, stop, resume, status    |
| `scheduler` | list, add, sync                |
| `activity`  | list                           |
| `server`    | health                         |
