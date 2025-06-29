#!/bin/bash
set -euo pipefail
rm -f /tmp/gpt-pilot-pty
APP_COMMAND="/APP/APP/23_gpt-pilot/gpt-pilot/venv/bin/python /APP/APP/23_gpt-pilot/gpt-pilot/main.py"
socat pty,raw,echo=0,link=/tmp/gpt-pilot-pty EXEC:"$APP_COMMAND"

