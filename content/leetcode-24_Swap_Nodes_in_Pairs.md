Title: 24. Swap Nodes in Pairs 
Date: 2016-09-21 18:23
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-24_Swap_Nodes_in_Pairs 
Authors: Weezer Su
Summary: Swap Nodes in Pairs


```python
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        first = head
        second = head.next
        head = second
        prev = None
        while first is not None and first.next is not None:
            first.next = second.next
            second.next = first
            if prev is None:
                prev = first
            else:
                prev.next = second
                prev = first
            first = first.next
            if first is not None:
                second = first.next
        return head
```
 
recursion
```python
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None or head.next == None:
            return head
        new_pair = head.next.next
        new_head = head.next
        head.next.next = head
        head.next = self.swapPairs(new_pair)
        return new_head
```
