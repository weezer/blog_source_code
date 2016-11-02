Title: 4. Median of Two Sorted Arrays
Date: 2016-10-22 20:49
Category: leetcode
Tags: code, python, leetcode
Slug: Median_of_Two_Sorted_Arrays 
Authors: Weezer Su
Summary: Median of Two Sorted Arrays

递归的方式我实在没想明白，边界实在太麻烦了。留下来以后慢慢弄把。

```python
   def findKth(self, A, B, k):
        if len(A) <= 0:
            return B[k - 1]
        if len(B) <= 0:
            return A[k - 1]
        if k == 1:
            return min(A[0], B[0])

        if (len(A) + len(B))/2 + 1 > k:
            if A[len(A)/2] > B[len(B)/2]:
                return self.findKth(A[:len(A)/2], B, k)
            else:
                return self.findKth(A, B[:len(B)/2], k)
        else:
            if A[len(A) / 2] > B[len(B) / 2]:
                return self.findKth(A, B[len(B)/2 + 1:], k - len(B)/2 - 1)
            else:
                return self.findKth(A[len(A)/2 + 1:], B, k - len(A)/2 - 1)
```

上面是kth element的递归，下面才是解法，用的是一直减掉k-1个element， 然后第k个就是了，减法用的二分。

```python
class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if (len(nums1) + len(nums2)) % 2 == 1:
            return self.findKth(nums1, nums2, (len(nums1) + len(nums2)) / 2)
        else:
            small = self.findKth(nums1, nums2, (len(nums1) + len(nums2)) / 2 - 1)
            big = self.findKth(nums1, nums2, (len(nums1) + len(nums2)) / 2)
            return (small + big) / 2.0
        
    def findKth(self, A, B, k):
        while k > 0:
            mid = (k - 1)/2
            if mid >= len(A):
                B = B[mid+1:]
            elif mid >= len(B) or A[mid] < B[mid]:
                A = A[mid+1:]
            else:
                B = B[mid+1:]
            k -= mid+1
        if len(A) <= 0:
            return B[0]
        if len(B) <= 0:
            return A[0]
        return min(A[0], B[0])
```

