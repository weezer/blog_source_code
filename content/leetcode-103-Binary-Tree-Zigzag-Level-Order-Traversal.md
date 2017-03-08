Title:103. Binary Tree Zigzag Level Order Traversal 
Date: 2017-03-07 23:07
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-103-Binary-Tree-Zigzag-Level-Order-Traversal 
Authors: Weezer Su
Summary: Binary Tree Zigzag Level Order Traversal


```python
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        import collections
        if root is None:
            return []
        current_level = collections.deque()
        current_level.append(root)
        return_answer = []
        flag = 1
        while current_level:
            inpurt_stack = list(current_level)
            return_answer.append([x.val for x in inpurt_stack[::flag]])
            print return_answer
            flag *= -1
            current_level_len = len(current_level)
            for i in range(current_level_len):
                current_node = current_level.popleft()
                if current_node.left:
                    current_level.append(current_node.left)
                if current_node.right:
                    current_level.append(current_node.right)
        return return_answer
```

