#!/bin/sh
git checkout main
git pull -r
git checkout -b day$1
touch day$1.py
touch input_day$1.txt
touch test_day$1.txt
git add .
git commit -m "Add new day $1"
git push --set-upstream origin day$1