Title: 29. Divide Two Integers 
Date: 2016-09-22 21:22
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-29_Divide_Two_Integers 
Authors: Weezer Su
Summary: Divide Two Integers

INT_MAX = (1 << 31) - 1, 还有就是 2 == 1 << 1
Binary Search for fun

```python
class Solution(object):
    def binarySearchDivide(self, dividend, divisor):
        right_num = dividend
        left_num = 0
        while True:
            mid_num = (right_num + left_num) / 2
            if (mid_num + 1) * divisor > dividend > mid_num * divisor or mid_num * divisor == dividend:
                return mid_num
            else:
                if mid_num * divisor > dividend:
                    right_num = (right_num + left_num) / 2
                else:
                    left_num = (right_num + left_num) / 2

```


convert into 
整数近似除法：32/3 = 10

显然求近似除法可以用乘法来二分查找：32 ~ 3*10 = 3*[1*(2^3) + 0*(2^2) + 1*(2^1) + 0*(2^0)]

res = 0

1. 先找到a使x*2^a <= y < x*2^(a+1)，res += 2^a，y = y - x*2^a

2. if(y >= x*2^(a-1) {res+=2^(a-1); y = y - x*2^(a-1);} 

3. if(y >= x*2^(a-2) {res+=2^(a-2); y = y - x*2^(a-2);}
```python
    def BinarySearchNoDivide(self, dividend, divisor):
        res = 0
        count = 1
        while dividend >= divisor:
            if divisor * (2 ** count) <= dividend < divisor * (2 ** (count + 1)):
                res += (2 ** count)
                dividend -= divisor * (2 ** count)
                count = 0
            else:
                count += 1
        return res
```

then the solution will be
```python
class Solution(object):
    def divide(self, dividend, divisor):
        INT_MAX = (1 << 31) - 1
        if divisor == 0:
            return INT_MAX
        neg_sign = dividend > 0 and divisor < 0 or dividend < 0 and divisor > 0
        abs_dividend, abs_divisor = abs(dividend), abs(divisor)
        answer, shift = 0, 31
        while shift >= 0:
            if abs_dividend >= abs_divisor << shift:
                abs_dividend -= abs_divisor << shift
                answer += 1 << shift
            shift -= 1
        if neg_sign:
            answer = -answer
        if answer > INT_MAX:
            return INT_MAX
        return answer
```
