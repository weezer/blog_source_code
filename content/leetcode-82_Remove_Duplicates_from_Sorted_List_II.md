Title: 82. Remove Duplicates from Sorted List II
Date: 2016-12-02 00:20
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-82_Remove_Duplicates_from_Sorted_List_II
Authors: Weezer Su
Summary: Remove Duplicates from Sorted List II

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
        pseudohead = ListNode(None)
        pseudohead.next = head

        if head is None:
            return head
        else:
            pseudohead.val = head.val
        current = pseudohead
        while current.next is not None:
            nextval = current.next
            if nextval.next is not None and nextval.val == nextval.next.val:
                nextval.next = nextval.next.next
                while nextval.next is not None and nextval.val == nextval.next.val:
                    nextval.next = nextval.next.next
                current.next = current.next.next
            else:
                current = current.next
        return pseudohead.next
```

