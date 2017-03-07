Title: 86. Partition List 
Date: 2017-02-12 23:24
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-86_Partition_List  
Authors: Weezer Su
Summary:  Partition List
最恨这种题目了。

```python
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if head is None or head.next is None:
            return head

        self.current = head

        self.small = ListNode(0)
        self.large = ListNode(0)
        self.smallhead = self.small
        self.largehead = self.large

        while self.current is not None:
            if self.current.val < x:
                self.small.next = self.current
                self.small = self.small.next
            else:
                self.large.next = self.current
                self.large = self.large.next
            self.current = self.current.next
        self.large.next = None
        self.small.next = self.largehead.next
        return self.smallhead.next
```

