#!/bin/bash

echo "updating..."
cp -r docs-content/content swarmdocs/
cp -r docs-content/img swarmdocs/static/
sleep 60

./reload.sh
