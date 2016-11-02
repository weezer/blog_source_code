Title: 21. Merge Two Sorted Lists 
Date: 2016-09-21 00:57
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-21_Merge_Two_Sorted_Lists 
Authors: Weezer Su
Summary: Merge Two Sorted Lists


```python
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        reserve_head = ListNode(0)
        point = reserve_head
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l2.next
            point = point.next
        if l1 is not None:
            point.next = l1
        if l2 is not None:
            point.next = l2
        return reserve_head.next
            
        
```

