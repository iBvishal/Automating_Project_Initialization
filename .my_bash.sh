#!/bin/bash

function create(){
    cd
    python create.py $1
    cd "$(cwd)$1"
    git init
    git remote add origin git@github.com:username/$1.git
    touch README.md
    git add .
    git commit -m "initial Commit"
    git push origin master
    vs .
}