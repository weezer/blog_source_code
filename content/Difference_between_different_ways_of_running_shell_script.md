Title:Difference between different ways of running shell script
Date:2018-10-15
Category: linux
Tags: tech
Slug: Difference_between_different_ways_of_running_shell_script
Authors: Weezer Su
Summary:Difference between different ways of running shell script
```sh test.sh```
Tells the command to use sh to execute test.sh.

```./test.sh```

Tells the command to execute the script. The interpreter needs to be defined in the first line with something like ```#!/bin/sh``` or ```#!/bin/bash```. Note that in this case the file ```test.sh``` needs to have execution rights for the user performing this command. Otherwise it will not be executed.

In both cases, all variables used will expire after the script is executed.

```. ./test.sh```

Sources the code. That is, it executes it and whatever executed, variables defined, etc, will persist in the session.


