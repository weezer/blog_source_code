Title: A note for bash tricks.
Date: 2017-09-29
Category: tech
Tags: code, tech
Slug: bash_trick
Authors: Weezer Su
Summary:all bash skills

What does it do?
```
export LOGFILE=$LOGDIRECTORY/${SCRIPT_NAME}.log
exec > >(tee $LOGFILE)
exec 2>&1
```

In shells, `exec` does 1) file openings and redirections 2) actual execing (replacing the current process image with another process image).

These execs are redirections.

First you redirect `(exec 1> >(tee $LOGFILE))` the stdout descriptor (1) to a process substitution-generated pipe connected to a concurrently run tee process that has $LOGFILE as its first argument and then you redirect the stderr descriptor (2) to the same place as where descriptor 1 now points (the tee pipe).

Keeping in mind that filedescriptors get inherited, you've just made all future stdout and stderr output go to the tee process, which writes it to $LOGFILE and to wherever filedescriptor 1 pointed to originally (probably your terminal).

> Note: The tee process outputs to the original stdout (=the original filedescriptor 1) because, as you can learn from /searching bash(1) for Simple Command Expansion and Process Substitution, process substitution ( >() <() ) happens (along with other expansions) before redirections get executed, which means that the redirection in exec 1> >(tee "$LOGFILE") happens after tee has started, leaving tee with the same filedescriptor 1 that it inherited from the parent shell. (If it were the other way around, tee would be made to write to its own input, which might make it deadlock, depending on its IO pattern).

