Title:97. Interleaving String 
Date: 2017-03-05 13:17
Category: leetcode
Tags: code, python, leetcode
Slug:leetcode-97-Interleaving-String 
Authors: Weezer Su
Summary:Interleaving String 

eg.
```s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"```
add an 0 in the front for future convinience. if the s3[i+j] == s1[j] and in the belowing matrix the matrix[i][j-1] is T, then we can
find the path to the next letter, mark it as True.

| X | 0  ,   | a  ,   | a  ,   | b  ,   | c  ,   | c   |
| ---- | ---- | ---- | ---- | ---- | ---- | ---- |
| 0 | T | T | T | F | F | F |
| d | F | F | T | T | F | F |
| b | F | F | T | T | T | F |
| b | F | F | T | F | F | F |
| c | F | F | T | T | T | F |
| a | F | F | F | F | T | T |

```python
ass Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        inter_matrix = [[False for i in range(len(s1) + 1)] for j in range(len(s2) + 1)]
        s3 = "0" + s3
        s1 = "0" + s1
        s2 = "0" + s2
        for i in range(len(inter_matrix)):
            for j in range(len(inter_matrix[0])):
                if i == 0 and j == 0:
                    inter_matrix[i][j] = True
                elif i == 0:
                    if s3[j] == s1[j]:
                        inter_matrix[i][j] = inter_matrix[i][j-1]
                elif j == 0:
                    if s3[i] == s2[i]:
                        inter_matrix[i][j] = inter_matrix[i-1][j]
                elif s3[i+j] == s1[j] and inter_matrix[i][j-1] or s3[i+j] == s2[i] and inter_matrix[i-1][j]:
                    print s3[i+j] + " : " + s1[j] + " : " + s2[i]
                    inter_matrix[i][j] = True
        print inter_matrix
        return inter_matrix[len(s2) - 1][len(s1) - 1]

if __name__ == "__main__":
    s = Solution()
    # print s.isInterleave("aabcc", "dbbca", "aadbbcbcac")
    # print s.isInterleave("aabcc", "dbbca", "aadbbbaccc")
    print s.isInterleave("db", "b", "cbb")
```

