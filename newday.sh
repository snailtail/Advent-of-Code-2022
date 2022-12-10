#!/bin/sh

#git checkout main
#git pull -r
#git checkout -b day$1

# mkdir day$1
python3 ./getinput.py $1
#cd day$1
touch $1.py
touch $1test.dat
echo "# :christmas_tree: Advent of Code 2022 Day$1 :christmas_tree:" > $1.md
git add .
git commit -m "Add new day $1"
git push --set-upstream origin day$1