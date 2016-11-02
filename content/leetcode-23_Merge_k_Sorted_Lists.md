Title: 23. Merge k Sorted Lists 
Date: 2016-09-21 17:33
Category: leetcode
Tags: code, python, leetcode
Slug:leetcode-23_Merge_k_Sorted_Lists 
Authors: Weezer Su
Summary: Merge k Sorted Lists, using heap, two sorted list merge or similar merge sort for k-lists.

heapq.heappush(), heapq.heappop(). [heap queue library from  python2](https://docs.python.org/2/library/heapq.html)
```python
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        pqueue = []
        for i in lists:
            if i:
                heapq.heappush(pqueue, (i.val, i))
        head = ListNode(0)
        current = head
        while pqueue:
            pop_out = heapq.heappop(pqueue)
            current.next = pop_out[1]
            current = current.next
            if pop_out[1].next is not None:
                heapq.heappush(pqueue, (pop_out[1].next.val, pop_out[1].next))
        return head.next
            
                
```

and also we can use the two sorted merge funtion to do this question but the time complexity will be squared.

```python
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        k_current =  None
        for i in lists:
            k_current = self.twoListMerge(k_current, i)
        return k_current
        
    def twoListMerge(self, list1, list2):
        head = ListNode(0)
        current = head
        while list1 is not None and list2 is not None:
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1= list1.next
            current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return head.next
        
            
```

and think for a little bit deeper, you can do a similar mergesort for this question.

```python
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if len(lists) == 0:
            return []
        end = len(lists) - 1
        while end > 0:
            start = 0
            while start < end:
                lists[start] = self.twoListMerge(lists[start], lists[end])
                start += 1
                end -= 1
        return lists[0]
        
    def twoListMerge(self, list1, list2):
        head = ListNode(0)
        current = head
        while list1 is not None and list2 is not None:
            if list1.val > list2.val:
                current.next = list2
                list2 = list2.next
            else:
                current.next = list1
                list1= list1.next
            current = current.next
        if list1:
            current.next = list1
        if list2:
            current.next = list2
        return head.next
```
