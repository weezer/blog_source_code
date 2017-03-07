#!/bin/bash

activate () {
  . bin/activate
}
activate

pelican content
cd output
git add .
if [ -z "$1" ]
then
  var=`git ls-files --others --exclude-standard | grep -v "tag"`
else
  var=$1  
fi
echo $var
git commit -m "\$var"
git push origin master
