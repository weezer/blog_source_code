Title: 61. Rotate List 
Date: 2016-11-01 23:25
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-61_Rotate_List 
Authors: Weezer Su
Summary: Rotate List


```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if head is None or k == 0:
            return head
        first_point = head
        second_point = head
        count = 1
        while second_point.next is not None:
            second_point = second_point.next
            count += 1
        second.next = head
        k %= count
        k = count - k
        while k > 1:
            first_point = first_point.next
```

