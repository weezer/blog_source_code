Title: 2. Add Two Numbers
Date: 2016-09-12 23:49
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-02-Add_Two_Numbers
Authors: Weezer Su
Summary: second question on leetcode

A stupid and slick question。
    
    
    :::python
    class Solution(object):
        def addTwoNumbers(self, l1, l2):
            """
            :type l1: ListNode
            :type l2: ListNode
            :rtype: ListNode
            """
            head = ListNode(0)
            cp = head
            carry = 0
            while True:
                if l1 is not None:
                    cp.val += l1.val
                    l1 = l1.next
                if l2 is not None:
                    cp.val += l2.val
                    l2 = l2.next
                if cp.val > 9:
                    carry = 1
                    cp.val = int(str(cp.val)[::-1][0])
                else:
                    carry = 0
                np = ListNode(carry)
                if l1 or l2 or carry:
                    cp.next = np
                    cp = np
                else:
                    break
            return head
                  
