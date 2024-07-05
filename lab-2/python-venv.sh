#!/bin/sh
: "3.12.3:=python"
mkdir "/v3.12.3"
python3 -m venv "/v3.12.3"
source "/v3.12.3/bin/activate"

exec "$@"