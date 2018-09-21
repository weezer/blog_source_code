Title: using subprocess and smtp and vmstat in python
Date: 2018-09-14 
Category: tech
Tags: code, python, tech
Slug: subprocess_smtp
Authors: Weezer Su
Summary: Subprocess and vmstat


```python
import subprocess
import threading
import smtplib


def output_reader(proc, count, threshold):
    for line in iter(proc.stdout.readline, ''):
        lst = line.split()
        if len(lst) >= 9 and lst[9].isdigit() and int(lst[9]) > threshold:
            count[0] += 1


def main():
    count = [0]
    proc = subprocess.Popen(['vmstat', '-n', '1'],
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)

    t = threading.Thread(target=output_reader, args=(proc, count, 200))
    t.start()

    try:
        while 1:
            if count[0] >= 5:
                # smtplib
                pass
    finally:
        proc.terminate()
        try:
            proc.wait()
            print "subprcess did terminate"
        except Exception as e:
            print 'subprocess did not terminate properly'
    t.join()

main()
```

