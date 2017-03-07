Title:99. Recover Binary Search Tree 
Date: 2017-03-05 20:37
Category: leetcode
Tags: code, python, leetcode
Slug:leetcode-99-Recover-Binary-Search-Tree 
Authors: Weezer Su
Summary:99. Recover Binary Search Tree 
如果是一个普通的list，其中有2个元素交换了位置，你会怎么做把他们换回来？同理， bst有一个特殊的遍历方式，inorder, 如果你使用inorder打印出来
的结果，和一个排好序的list是一样的，如果这样，你就该考虑如何将list交换的方式套用到inorder上面。下面2个小snippets，第一个就是list交换，然后
解决了bst的问题。
```python
temp = []
for i in range(10):
    temp.append(i)
temp[3], temp[7] = temp[7], temp[3]

print temp

lst_len = len(temp)
pos1 = None
pos2 = None
for pos in range(1, lst_len):
    if pos1 is None and temp[pos] < temp[pos-1]:
        pos1 = pos-1
    if pos1 is not None and temp[pos] < temp[pos-1]:
        pos2 = pos

temp[pos1], temp[pos2] = temp[pos2], temp[pos1]

print temp
```

```python
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.pos1 = None
        self.pos2 = None
        self.prev = None
        head = root
        def inorder(root):
            if root.left:
                inorder(root.left)
            if self.prev is not None and self.prev.val > root.val and self.pos1 is None:
                self.pos1 = self.prev
            if self.pos1 is not None and self.prev.val > root.val:
                self.pos2 = root
            self.prev = root
            if root.right:
                inorder(root.right)
        inorder(root)
        self.pos1.val, self.pos2.val = self.pos2.val, self.pos1.val

        def inorder_traversal(root):
            if root.left:
                inorder_traversal(root.left)
            print root.val
            if root.right:
                inorder_traversal(root.right)
        inorder_traversal(head)

if __name__ == "__main__":
    root = TreeNode(6)
    head = root
    root.left = TreeNode(3)
    root = root.left
    root.left = TreeNode(1)
    root.right = TreeNode(4)
    root = head
    root.right = TreeNode(7)
    root = root.right
    root.left = TreeNode(8)
    root.right = TreeNode(10)
    root = root.right
    root.left = TreeNode(9)
    root.right = TreeNode(11)

    s = Solution()
    s.recoverTree(head)

```

