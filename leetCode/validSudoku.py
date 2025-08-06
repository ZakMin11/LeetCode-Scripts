'''Zak mineiko
leetcode 36. Valid Sudoku
Medium
incomplete
run time:
memory: 
'''


def isValidSudoku(board):
    l = len(board)    
    for x in range(l):
        for y in range(l):
            if board[x][y] != '.':
                if checkRowAndColFor(board[x][y], x, y) != [0,0]: # breaks row/col rule
                    return False

    return True
def checkCube(num, x,y):
    cube = {
        1: [0,0],
        2: [0,2],
        3: [0,6],
        4: [1,0],
        5: [1,2],
        6: [1,6],
        7: [2,0],
        8: [2,2],
        9: [2,6],
        }
    occur = 1
    #compute cube:
    start = [0,0]
    for i in range(cube):
        if (x>=cube[i].value() and x< = cube[i+1].value()) and ((y>=cube[i].value() and y< = cube[i+1].value()):
            start = cube[i].key()
    for i in range(3):
        for j in range(3):
            if board[start[0] + i, start[y] + 1] == num:
                occur+=1
    if occur > 2:           
        return False
    return True
def checkRowAndColFor(num, x, y):
    # returns [0,0] if num not in row or col
    #         [1,0] if num in row not col
    #         [0,1] if num in col not row
    #         [1,1] if num in col and row
    ret = [0,0]
    isRow = False
    # check rowi
    if board[x].count(num) > 1:
        ret = [1,0]
        isRow = True

    # check col
    occur = 1
    for row in board:
        if row[y] == num:
            occur+=1
    if occur >2:
        ret[1] = 1
    # for x in range(9):
    #     if x != int(num):
    #         if board[x][y] == num:
    #             ret = [0,1]
    #             if isRow:
                    # ret = [1,1]

    return ret

# board = [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]

board = [["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(isValidSudoku(board))
