Title: Reservoir Sampling (not finished)
Date: 2018-10-11
Category: leetcode
Tags: code, python, leetcode
Slug:Reservoir_Sampling
Authors: Weezer Su
Summary:Reservoir Sampling

https://gregable.com/2007/10/reservoir-sampling.html

when you are dealing with sampling issue, like:

1. analyze 1,000 reports from 100,000,000 reports
2. a name analysis base on 1,000 names from a yellow book
3. google "Ken Thompson", get 100 results randomly and found out which belongs to this yr

with those questions you dont know the size, the reservoir sampling algorithm is very important for saving your time and compute resource.

# Reservoir Sampling Algorithm

assume you have an input dataset size of  **n**, and the sampling size of  **k**, first you build up a list can store **k** elements, put the first k element from the input to the list, from the **k + 1** element, 

$k+1 \div k$ 

$\displaystyle\frac{b}{c+d}$

$\frac{b}{c+d}$

```python
import random
def reservoir_func():
    size = 4
    lst = []
    for i in range(1000):
        if i < size:
            lst.append(i)
        else:
            j = random.randint(0, i)
            if j < size:
                lst[j] = i
    print lst
```

