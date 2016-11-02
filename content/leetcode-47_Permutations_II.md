Title: 47. Permutations II 
Date: 2016-10-14 01:05
Category: leetcode
Tags: code, python, leetcode
Slug:leetcode-47_Permutations_II 
Authors: Weezer Su
Summary:  Permutations II


```pythoni
class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        self.result = []
        if num is None:
            return []
        if len(num) == 0:
            return [[]]
        self.permutation([], sorted(num))
        return self.result

    def permutation(self,  temp, num):
        if len(num) == 0:
            self.result.append(temp)
        else:
            for i in range(len(num)):
                if i > 0 and num[i] == num[i - 1]:
                    continue
                self.permutation( temp + [num[i]], num[:i] + num[i + 1:])
```

