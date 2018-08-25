Title: 303 Range Sum Query - Immutable
Date: 2018/08/07
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-303_Range_Sum_Query-Immutable
Authors: Weezer Su
Summary: 303 Range Sum Query - Immutable

Segment Tree

```python
class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.len_nums = len(nums)
        self.seg_arr = [0] * self.len_nums
        self.seg_arr += nums
        for i in range(self.len_nums-1, 0, -1):
            self.seg_arr[i] = self.seg_arr[i*2] + self.seg_arr[i*2+1]
        print self.seg_arr

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        i += self.len_nums
        diff = self.seg_arr[i] - val
        while i > 0:
            self.seg_arr[i] -= diff
            i /= 2


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        left = i + self.len_nums
        right = j + self.len_nums
        if i > j:
            return 0
        if i == j:
            return self.seg_arr[left]
        result = 0
        while left <= right:
            if left & 1 == 1:
                result += self.seg_arr[left]
                left += 1
            if right & 1 == 0:
                result += self.seg_arr[right]
                right -= 1
            left >>= 1
            right >>= 1
        return result



        # Your NumArray object will be instantiated and called as such:
        # obj = NumArray(nums)
        # obj.update(i,val)
        # param_2 = obj.sumRange(i,j)

if __name__ == "__main__":
    s = NumArray([1,2,3,4,5,6,7,8,9])
    print s.sumRange(0, 0)
```

