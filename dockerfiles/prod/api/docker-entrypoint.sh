#!/bin/bash -ex

exec uvicorn webapi.app:app --host 0.0.0.0 --port ${PORT}
