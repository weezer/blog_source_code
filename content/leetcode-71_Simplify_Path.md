Title: 71. Simplify Path 
Date: 2016-11-02 23:59
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-71_Simplify_Path 
Authors: Weezer Su
Summary: Simplify Path 

```python
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        pathlst = path.split("/")
        remain_lst = []
        for i in pathlst:
            if i == '' or i == '.' or i == '..' and len(remain_lst) == 0:
                continue
            elif i == "..":
                remain_lst.pop()
            else:
                remain_lst.append(i)
        return "/" + "/".join(remain_lst)
```

