Title: 145. Binary Tree Postorder Traversal 
Date: 2017-03-10 00:59
Category: leetcode
Tags: code, python, leetcode
Slug:leetcode-145-Binary-Tree-Postorder-Traversal 
Authors: Weezer Su
Summary: Binary Tree Postorder Traversal


```python
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        import collections
        return_queue = collections.deque()
        stack = []
        if not root:
            return stack
        else:
            stack.append(root)
        while stack:
            current = stack.pop()
            return_queue.appendleft(current.val)
            if current.left:
                stack.append(current.left)
            if current.right:
                stack.append(current.right)

        print return_queue

if __name__ == "__main__":
    root = TreeNode(6)
    head = root
    root.left = TreeNode(3)
    root = root.left
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root = head
    root.right = TreeNode(8)
    root = root.right
    root.left = TreeNode(7)
    root.right = TreeNode(10)
    root = root.right
    root.left = TreeNode(9)
    root.right = TreeNode(11)

    s = Solution()
    s.postorderTraversal(head)
```

