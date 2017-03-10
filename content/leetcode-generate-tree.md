Title:Generate Tree 
Date: 2017-03-10 11:40
Category: leetcode
Tags: code, python, leetcode
Slug:leetcode-generate-tree 
Authors: Weezer Su
Summary: Generate Tree

So annoying to generate tree by hand

```python
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def generate_tree(nums):
    import collections
    q = collections.deque()
    q.extend(nums)
    node_queue = collections.deque()
    head_node = TreeNode(q.popleft())
    node_queue.append(head_node)
    while node_queue:
        current = node_queue.popleft()
        if not current:
            continue
        if not q:
            break
        v1 = q.popleft()
        if v1 is not "#":
            left = TreeNode(v1)
            current.left = left
            node_queue.append(left)
        v2 = q.popleft()
        if v2 is not "#":
            right = TreeNode(v2)
            current.right = right
            node_queue.append(right)
    return head_node
```

