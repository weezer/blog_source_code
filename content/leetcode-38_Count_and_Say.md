Title: 38. Count and Say 
Date: 2016-09-29 23:03
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-38_Count_and_Say 
Authors: Weezer Su
Summary: Count and Say


```python
class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        if n == 1:
            return "1"
        theNum = 1
        for i in range(n - 1):
            theNum = self.str_generator(int(theNum))
        return theNum

    def str_generator(self, n):
        str_n = str(n)
        flag = str_n[0]
        count = 0
        answer = []
        for i in str_n:
            if i != flag:
                answer.append(count)
                answer.append(flag)
                flag = i
                count = 1
            else:
                count += 1
        answer.append(count)
        answer.append(flag)

        return ''.join(map(str, answer))
```

