Title: 85. Maximal Rectangle
Date: 2017-02-21 12:37
Category: leetcode
Tags: code, python, leetcode
Slug: 85_Maximal-Rectangle 
Authors: Weezer Su
Summary: Maximal Rectangle

```python
ass Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        largest = 0
        my_matrix = []
        for i in matrix:
            my_matrix.append(map(int, list(i)))
        matrix = my_matrix
        print matrix
        for i in range(1, len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 1:
                    matrix[i][j] = matrix[i-1][j] + 1
        print matrix
        for i in matrix:
            largest = max(largest, self.largestRectangleArea(i))
        return largest

    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        dummy_stack = heights[:] + [0]
        stack = []
        largest = 0
        pos = 0
        while pos < len(dummy_stack):
            if not stack or dummy_stack[pos] > dummy_stack[stack[-1]]:
                stack.append(pos)
                pos += 1
            else:
                cur_pos = stack.pop()
                largest = max(largest, dummy_stack[cur_pos] * (not stack and pos or pos - stack[-1] - 1))
        return largest
```

