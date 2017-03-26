Title: little blog helper bash scripts
Date: 2017-03-11 01:52
Category: tech
Tags: code, bash, tech
Slug: little_blog_helper
Authors: Weezer Su
Summary: Little blog helper bash scripts

can save my life to publish those leetcode codes.
```bash
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

```

```bash
#!/usr/bin/env bash

input="$1"
file_name="leetcode-""${input// /-}"
file_name="${file_name/./}"
echo content/"$file_name"".md"
echo $input
cp content/leetcode_template content/$file_name".md"

sed -i '' "/^Title:/ s/$/ $input/" content/"$file_name"".md"
sed -i '' "/^Date:/ s/$/ $(date +"%Y-%m-%d %H:%M:%S")/" content/"$file_name"".md"
sed -i '' "/^Slug:/ s/$/ $file_name/" content/"$file_name"".md"
sed -i '' "/^Summary:/ s/$/ $input/" content/"$file_name"".md"

cat ../PycharmProjects/very_old_scripts/testPydev/"$input".py
echo
sed -i '' "/python$/r "../PycharmProjects/very_old_scripts/testPydev/"$input".py"" content/"$file_name"".md"
echo "\`\`\`" >> content/"$file_name"".md"
```
