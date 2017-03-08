Title:104. Maximum Depth of Binary Tree 
Date: 2017-03-07 23:20
Category: leetcode
Tags: code, python, leetcode
Slug:leetcode-104-Maximum-Depth-of-Binary-Tree 
Authors: Weezer Su
Summary: Maximum Depth of Binary Tree

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        import collections
        stack = collections.deque()
        answer = 0
        if root is None:
            return answer
        stack.append(root)
        while stack:
            stack_len = len(stack)
            answer += 1
            for i in range(stack_len):
                current = stack.popleft()
                if current.left is not None:
                    stack.append(current.left)
                if current.right is not None:
                    stack.append(current.right)
        return answer
```

