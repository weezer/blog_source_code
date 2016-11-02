Title: 36. Valid Sudoku 
Date: 2016-09-29 22:30
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-36_Valid_Sudoku 
Authors: Weezer Su
Summary: Valid Sudoku

Interesting one, went over the set and know how to create unique number by square.


```python
class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [set([]) for i in range(9)]
        col = [set([]) for i in range(9)]
        square = [set([]) for i in range(9)]
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                num = int(board[i][j])
                if num in row[i]:
                    return False
                if num in col[j]:
                    return False
                
                square_num = i / 3 * 3 + j / 3
                if num in square[square_num]:
                    return False
                row[i].add(num) 
                col[j].add(num)
                square[square_num].add(num)
        return True
```

