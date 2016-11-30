Title: 66. Plus One 
Date: 2016-11-02 00:48
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-66_Plus_One 
Authors: Weezer Su
Summary: Plus One


```pythoni
class Solution:
    # @param digits, a list of integer digits
    # @return a list of integer digits
    def plusOne(self, digits):
        reverse_digits = digits[::-1]
        if reverse_digits[0] + 1 == 10:
            carry = 1
        else:
            reverse_digits[0] += 1
            return reverse_digits[::-1]
        for pos, val in enumerate(reverse_digits):
            if val+carry == 10:
                carry = 1
                reverse_digits[pos] = 0
            else:
                reverse_digits[pos] = val + carry
                carry = 0
        if carry == 1:
            reverse_digits.append(1)
        return reverse_digits[::-1]
```

