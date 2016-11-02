Title: 17. Letter Combinations of a Phone Number 
Date: 2016-09-20 15:34
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-17_Letter_Combinations_of_a_Phone_Number 
Authors: Weezer Su
Summary: Letter Combinations of a Phone Number

Dont think its a medium level question.


```python
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        keyboard = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs',
                    '8': 'tuv', '9': 'wxyz'}
        result = []

        if len(digits) == 0:
            return []

        for i in digits:
            if len(result) == 0:
                result += list(keyboard[i])
                continue
            for j in range(len(result)):
                temp = result.pop(0)
                temp_list = keyboard[i]
                for z in temp_list:
                    result.append(temp + z)

        return result
```

