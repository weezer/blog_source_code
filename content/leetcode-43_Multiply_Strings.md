Title: 43. Multiply Strings 
Date: 2016-10-13 23:55
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-43_Multiply_Strings 
Authors: Weezer Su
Summary: Multiply Strings

```python
def multiply(num1, num2):
    return str(int(num1) * int(num2))
```

I'm joking.

```python
class Solution:
    # @param num1, a string
    # @param num2, a string
    # @return a string
    def multiply(self, num1, num2):
        result = 0
        pos1 = 0
        for i in num1[::-1]:
            pos = 0
            for j in num2[::-1]:
                first = ord(i) - ord('0')
                second = ord(j) - ord('0')
                result += first * second * (10 ** pos) * (10 ** pos1)
                pos += 1
            pos1 += 1
        return str(result)
```

