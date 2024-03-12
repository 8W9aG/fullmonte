#!/bin/sh

set -e

git push origin main
rm -rf dist
python setup.py sdist
twine upload --skip-existing dist/* --verbose
