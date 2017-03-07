Title: 8 皇后 
Date: 2017-02-23 15:07
Category: leetcode
Tags: code, python, leetcode
Slug: leetcode-8-queue 
Authors: Weezer Su
Summary: 8 皇后

哎，居然花了好几个小时, 妈的，还写错了。

```python
def eight_queue():
    for i in range(4):
        board_stack = [i]
        generate_8_queue(board_stack)


def generate_8_queue(board):
    if len(board) == 4:
        print board
        return
    i = len(board)
    for j in range(4):
        if can_fit(i, j, board):
            cpy_board = board[:]
            cpy_board.append(j)
            generate_8_queue(cpy_board)


def can_fit(i, j, board):
    for k, v in enumerate(board):
        if j == v or abs(i - k) == abs(j - v):
            return False
    return True


eight_queue()
```

