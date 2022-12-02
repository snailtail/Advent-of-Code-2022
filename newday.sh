#!/bin/sh
git checkout main
git pull -r
git checkout -b day$1
mkdir day$1
cd day$1
touch day$1.py
touch day$1_input.txt
touch day$1_testinput.txt
echo "# :christmas_tree: Advent of Code 2022 Day$1 :christmas_tree:" > README.md
git add .
git commit -m "Add new day $1"
git push --set-upstream origin day$1