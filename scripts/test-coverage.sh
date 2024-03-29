#!/bin/sh -e
set -x

python -m pip install --upgrade pip
pip install flake8 pytest pytest-cov

pytest --cache-clear --no-cov-on-fail
coverage report -m --omit src/biocli/_biocli.py