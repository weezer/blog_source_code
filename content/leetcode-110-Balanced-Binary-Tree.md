Title: 110. Balanced Binary Tree
Date: 2017-03-27 14:18:54
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-110-Balanced-Binary-Tree
Authors: Weezer Su
Summary: 110. Balanced Binary Tree


```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return None
        def dfs(node):
            if not node:
                return 0
            else:
                return max(dfs(node.left), dfs(node.right)) + 1

        lt = dfs(root.left)
        rt = dfs(root.right)
        if abs(lt - rt) > 1:
            return False
        else:
            return self.isBalanced(root.left) and self.isBalanced(root.right)```

```
