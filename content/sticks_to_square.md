Title: Stcicks can make a square 
Date: 2016-11-14 00:11
Category: leetcode
Tags: code, python, leetcode
Slug:sticks_to_square 
Authors: Weezer Su
Summary: 一堆火柴能不能组成正方形

题目是，有一个list的火柴，长短不一，能不能组成正方形，要求火柴用完，也不能折。用了一个动归的方法就是n个数能不能生成一个制定数。
```python

def makesquare(lst):
    num = sum(lst) // 4
    if len(lst) < 4 or num * 4 != sum(lst):
        return False
    for _ in range(3):
        return_lst = canmakenumber(lst, num)
        if return_lst is False:
            return False
        for i in return_lst:
            lst.remove(i)
    return True


def canmakenumber(lst, num):
    b = [0] * num
    b2 = [0] * num
    can_make = False
    for pos, i in enumerate(lst):
        for j in b:
            if j != 0 and j-1+i < num:
                b2[j-1+i] = b[j-1] + i
            if b2[num-1] != 0:
                can_make = True
                break
        b2[i - 1] = i
        b = b2[:]
        if can_make:
            bb = findthesticks(b, lst[:pos+1])
            break
    if can_make:
        return bb
    return False


def findthesticks(lst, input_stick):
    return_lst = []
    # print input_stick
    # print lst
    pos = len(lst) -1
    for i in input_stick[::-1]:
        if lst[pos] in input_stick:
            return_lst.append(lst[pos])
            break
        elif lst[pos - i] != 0:
            return_lst.append(i)
            pos -= i
    return return_lst



print makesquare([6,3,3,2,2,5,2,2,5,5,10])


```
