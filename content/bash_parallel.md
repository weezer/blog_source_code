Title: bash parallel
Date: 2018-11-07
Category: tech
Tags: code, bash, tech
Slug: bash_parallel
Authors: Weezer Su
Summary: bash parallel

bash run jobs parallel.
```bash

#!/bin/bash
 
#start timer
begin=$(date +%s)
 
#create test folder
root_dir="/home/test"
 
if [ ! -d $root_dir ]; then
	mkdir -p $root_dir
fi
cd $root_dir
 
#create folder, it's a example.
function create_dir()
{
 
	mkdir $1
}
 
#need 10,000 folders
count=10000
rsnum=200
cishu=$(expr $count / $rsnum)
 
for ((i=0; i<$cishu;))
do
	start_num=$(expr $i \* $rsnum + $i)
	end_num=$(expr $start_num + $rsnum)
	for j in `seq $start_num $end_num`
	do
		create_dir $j &
	done
	wait
	i=$(expr $i + 1)
done
 
#timeit
end=$(date +%s)
spend=$(expr $end - $begin)
echo "spend $spend s"
```

