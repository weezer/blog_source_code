#!/bin/bash

activate () {
  source bin/activate
}

activate

pelican content
cd output
git add .
if [ -z "$1" ]
then
  var=`git status --porcelain | grep "^A" | cut -c 4-`
else
  var=$1  
fi
echo $var
git commit -m "$var"
git push origin master
