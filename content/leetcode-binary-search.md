Title: Binary Search
Date:2018-08-13
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-binary-search
Authors: Weezer Su
Summary:binary search


```python
def binary_search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) / 2
        if nums[mid] == target:
            return True
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    return False


def binary_search_rank(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) / 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            l = mid + 1
        else:
            r = mid - 1
    return l

# with duplicate elements, If L < n and A[L] = T, then AL is the leftmost element that equals T.
# Even if T is not in the array, L is the rank of T in the array,
# or the number of elements in the array that are less than T.

# equals to bisect.bisect_leftmost()

def binary_search_leftmost(nums, target):
    l, r = 0, len(nums)
    while l < r:
        mid = (l + r) / 2
        if nums[mid] < target:
            l = mid + 1
        else:
            r = mid
    return l

# If L > 0 and A[L - 1] = T, then A[L - 1] is the rightmost element that equals T.
# Even if T is not in the array, n - (L - 1) is the number of elements in the array that are greater than T.


#equals to bisect.bisect()

def binary_search_rightmost(nums, target):
    l, r = 0, len(nums)
    while l < r:
        mid = (l + r) / 2
        if nums[mid] <= target:
            l = mid + 1
        else:
            r = mid
    return l - 1
```
Rank queries can be performed with the procedure for finding the leftmost element must be used. The number of elements less than the target value is returned by the procedure.

Predecessor queries can be performed with rank queries. If the rank of the target value is r, its predecessor is r − 1.

For successor queries, the procedure for finding the rightmost element can be used. If the result of running the procedure for the target value is r, then the successor of the target value is r + 1.

The nearest neighbor of the target value is either its predecessor or successor, whichever is closer.


```python
def index(a, x):
    'Locate the leftmost value exactly equal to x'
    i = bisect_left(a, x)
    if i != len(a) and a[i] == x:
        return i
    raise ValueError

def find_lt(a, x):
    'Find rightmost value less than x'
    i = bisect_left(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_le(a, x):
    'Find rightmost value less than or equal to x'
    i = bisect_right(a, x)
    if i:
        return a[i-1]
    raise ValueError

def find_gt(a, x):
    'Find leftmost value greater than x'
    i = bisect_right(a, x)
    if i != len(a):
        return a[i]
    raise ValueError

def find_ge(a, x):
    'Find leftmost item greater than or equal to x'
    i = bisect_left(a, x)
    if i != len(a):
        return a[i]
    raise ValueError
```
