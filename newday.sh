#!/bin/sh
git checkout main
git pull -r
git checkout -b day$1
touch day$1.py
touch day$1_input.txt
touch day$1_test.txt
touch day$1.md
git add .
git commit -m "Add new day $1"
git push --set-upstream origin day$1