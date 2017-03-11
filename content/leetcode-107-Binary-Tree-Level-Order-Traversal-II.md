Title:107. Binary Tree Level Order Traversal II 
Date: 2017-03-10 22:05
Category: leetcode
Tags: code, python, leetcode
Slug:leetcode-107-Binary-Tree-Level-Order-Traversal-II 
Authors: Weezer Su
Summary:  Binary Tree Level Order Traversal II


```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return[]
        import collections
        q = collections.deque()
        answer = collections.deque()
        q.append(root)
        while q:
            answer.appendleft([x.val for x in q])
            q_len = len(q)
            for i in range(q_len):
                current = q.popleft()
                if current.left:
                    q.append(current.left)
                if current.right:
                    q.append(current.right)
        return list(answer)
```

