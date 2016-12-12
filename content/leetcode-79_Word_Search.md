Title: 79. Word Search 
Date: 2016-11-30 23:15
Category: leetcode
Tags: code, python, leetcode
Slug:leetcode-79_Word_Search 
Authors: Weezer Su
Summary: Word Search
先来个maze练练手
```python
grid = [[0, 0, 0, 0, 0, 1],
        [1, 1, 0, 0, 0, 1],
        [0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 0, 1],
        [0, 1, 0, 0, 1, 0],
        [0, 1, 0, 0, 0, 2]]


def search(x, y):
    if grid[x][y] == 2:
        return True
    elif grid[x][y] == 1:
        return False
    elif grid[x][y] == 3:
        return False

    grid[x][y] = 3

    if (x > 0 and search(x-1, y)) or (x + 1 < len(grid) and search(x+1, y)) or (y > 0 and search(x, y-1)) or\
                                             (y+1 < len(grid[0]) and search(x, y+1)):
        return True
    return False

print search(0, 0)
```
DFS, 剪枝没剪好，以后再说吧。
```python
class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        self.board = board
        self.word = word
        self.col = len(board[0])
        self.row = len(board)
        self.flag = False
        # arrived = [[0 for i in range(self.col)] for j in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                if board[i][j] == word[0]:
                    rest_word = word[1:]
                    arrived = [[0 for x in range(self.col)] for y in range(self.row)]
                    self.find_word(i, j, arrived, rest_word)
                if self.flag:
                    return self.flag
        return self.flag

    def find_word(self, row_num, col_num, arrived_matrix, rest_word):
        if len(rest_word) == 0:
            self.flag = True
            return
        arrived_matrix = [x[:] for x in arrived_matrix]
        arrived_matrix[row_num][col_num] = 1
        the_word = rest_word[:]
        # print the_word
        # print arrived_matrix
        if row_num-1 >= 0 and arrived_matrix[row_num-1][col_num] != 1 and the_word[0] == self.board[row_num-1][col_num]:
            self.find_word(row_num - 1, col_num, arrived_matrix[:], the_word[1:])
        if row_num+1 < self.row and arrived_matrix[row_num+1][col_num] != 1 and the_word[0] == self.board[row_num+1][
                    col_num]:
            self.find_word(row_num + 1, col_num, arrived_matrix[:], the_word[1:])
        if col_num-1 >= 0 and arrived_matrix[row_num][col_num-1] != 1 and the_word[0] == self.board[row_num][col_num-1]:
            self.find_word(row_num, col_num - 1, arrived_matrix[:], the_word[1:])
        if col_num+1 < self.col and arrived_matrix[row_num][col_num+1] != 1 and the_word[0] == self.board[row_num][
                    col_num+1]:
            self.find_word(row_num, col_num + 1, arrived_matrix[:], the_word[1:])
        if self.flag == True:
            return True
        else:
            return False
```

