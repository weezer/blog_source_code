Title:236. Lowest Common Ancestor of a Binary Tree 
Date: 2017-03-08 17:41
Category: leetcode
Tags: code, python, leetcode
Slug:leetcode-236-Lowest-Common-Ancestor-of-a-Binary-Tree 
Authors: Weezer Su
Summary: Lowest Common Ancestor of a Binary Tree


```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if not root or root == p or root == q: return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right
```
如果有点不存在，上面那个就废了，下面这个纪录所有点的path
```python
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        self.pos1 = []
        self.pos2 = []
        if root is None:
            return None

        def dfs(root, stack):
            if self.pos1 and self.pos2:
                return
            if root == p:
                self.pos1 = stack[:]
            if root == q:
                self.pos2 = stack[:]
            if root.left:
                tmp = stack[:]
                tmp.append(root.left)
                dfs(root.left, tmp)
            if root.right:
                tmp = stack[:]
                tmp.append(root.right)
                dfs(root.right, tmp)
        dfs(root,[root])
        self.pos1.append(True)
        self.pos2.append(False)
        stack_len = min(len(self.pos1), len(self.pos2))
        for i in range(stack_len):
            if self.pos1[i] != self.pos2[i]:
                return self.pos1[i-1]
        return None
```

