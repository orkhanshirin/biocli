#!/usr/bin/env bash

set -e
set -x

flake8
black biocli --check --diff
isort biocli --check --diff