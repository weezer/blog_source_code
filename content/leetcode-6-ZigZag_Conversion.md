Title: 06. ZigZag Conversion
Date: 2016-09-16 00:38
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-6-ZigZag_Conversion
Authors: Weezer Su
Summary: ZigZag Conversion

a ease question but spent me few time.
more like a math question, find the pattern between each line and numbers.


   |   |   |   |            
 ----:|----:|-----:|:----:|----:
 1  |   | 5 |   | 9
 2  | 4 | 6 | 8 | 10
 3  |   | 7 |   | 11
 ___ | ___ | ___ | ___ | ___



```python
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if len(s) <= 1 or numRows <= 1:
            return s
        rlst = []
        for i in range(numRows):
            pos = i
            gap1 = 2 * numRows - (i + 1) * 2
            gap2 = 2 * numRows - 2 - gap1
            gaps = [gap1, gap2]
            interval = 0
            while pos < len(s):
                if gaps[interval] != 0:
                    rlst.append(s[pos])
                    pos += gaps[interval]
                interval = (interval + 1) % 2
        return ''.join(rlst)
```	
