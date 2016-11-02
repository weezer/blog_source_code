Title: 12. Integer to Roman 
Date: 2016-09-18 00:25
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-12_Integer_to_Roman 
Authors: Weezer Su
Summary: Integer to Roman


```python
class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        roman_dict = {1: 'I', 4: 'IV', 5: 'V', 9: 'IX', 10: 'X', 40: 'XL',
        50: 'L', 90: 'XC', 100: 'C', 400: 'CD', 500: 'D', 900: 'CM', 1000: 'M'}
        r_lst = []

        digit = 1
        while num > 0:
            a_lst = []
            reminder = num % 10
            reminder *= digit
            digit *= 10
            num /= 10
            if roman_dict.get(reminder) is not None:
                r_lst.insert(0, roman_dict.get(reminder))
            else:
                for minus_num in sorted(roman_dict, reverse = True):
                    if reminder == 0:
                        break
                    if minus_num > reminder:
                        continue
                    else:
                        while reminder >= minus_num:
                            a_lst.append(roman_dict[minus_num])
                            reminder -= minus_num

            r_lst.insert(0, ''.join(a_lst))
        return ''.join(r_lst)

```
