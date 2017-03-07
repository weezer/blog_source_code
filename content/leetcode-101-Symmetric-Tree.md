Title:101. Symmetric Tree 
Date: 2017-03-05 21:13
Category: leetcode
Tags: code, python, leetcode
Slug:leetcode-101-Symmetric-Tree 
Authors: Weezer Su
Summary: Symmetric Tree

```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root is None:
            return True
        def checkNodes(leftNode, rightNode):
            if leftNode == rightNode:
                return True
            if leftNode is None or rightNode is None or leftNode.val != rightNode.val:
                return False
            return checkNodes(leftNode.left, rightNode.right) and checkNodes(leftNode.right, rightNode.left)
        return checkNodes(root.left, root.right)
```

