Title: 46. Permutations 
Date: 2016-10-14 00:03
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-46_Permutations 
Authors: Weezer Su
Summary: Permutations 
1,2,3 -> [1] -> [1,2], [2,1] -> [3,1,2], [1,3,2], [1,2,3], [3,2,1], [2,3,1], [2,1,3]

```python
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permute(self, num):
        aStack = []
        bStack = []
        
        if len(num) <= 1:
            return [num]
        else:
            if len(aStack) == 0:
                aStack.append([num.pop()])
            for i in num:
                bStack = []
                while len(aStack) > 0:
                    current = aStack.pop()
                    for j in range(len(current) + 1):
                        bStack.append(current[:j] + [i] + current[j:])
                aStack = bStack[:]
            return aStack    
```

