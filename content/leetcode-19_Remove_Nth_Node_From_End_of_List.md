Title: 19. Remove Nth Node From End of List 
Date: 2016-09-21 00:05
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-19_Remove_Nth_Node_From_End_of_List 
Authors: Weezer Su
Summary: Remove Nth Node From End of List

learned how to use python reference.


```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        temp = ListNode(0)
        temp.next = head
        return_node = temp
        for i in range(n):
            head = head.next
        while head is not None:
            head = head.next
            temp = temp.next
        temp.next = temp.next.next
        return return_node.next
```

