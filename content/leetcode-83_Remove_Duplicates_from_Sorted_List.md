Title: 83. Remove Duplicates from Sorted List 
Date: 2016-12-01 23:38
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-83_Remove_Duplicates_from_Sorted_List 
Authors: Weezer Su
Summary: Remove Duplicates from Sorted List

I DO HATE THIS QUESTION
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        current = head
        while current is not None and current.next is not None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next
        return head
```

