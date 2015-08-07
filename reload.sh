#!/bin/bash

echo "rebuilding..."
rm -rf swarmdocs/public/*
rm -rf swarmdocs/content
rm -rf swarmdocs/static/img
cp -r docs-content/content swarmdocs/
cp -r docs-content/img swarmdocs/static/
sleep 60

./reload.sh
