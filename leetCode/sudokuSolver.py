'''Zak mineiko
leetcode 37. Sudoku Solver
Hard
incomplete
run time:
memory:
'''

'''

The plan is to iterate through each square and check each open suare for row/col violations
and delete available numbers. Collect dictionary of all possible values for each empty cell,
only update the rows/cols affected when number is placed,


cube1Dict, cube2Dict, ..., cube9Dict = {1: '.', 2: '5', ..., 9: '.'}

cube1X = 3
cube1Y = 3

cube2X = 6
cube2Y = 3

cube3X = 9
cube3Y = 3
...

just check for cube number when needed

for x in range(9):
    for y in range(9):
        x+=1
        y+=1
        if x<=cube1Coords[0] and y<=cube1Coords[1]:
            # in cube 1
    i = i+1
    if i < 3


'''

def solveSudoku(board) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        [x,y,x2,y2]
        table = [[],

                ]

        possibleNums = ['1','2','3','4','5','6','7','8','9']
        possNums = [1,2,3,4,5,6,7,8,9]
        #quad0Numbers = board[0:3][0:3]
        quad0Numbers = board[0][0:3] + board[1][0:3] + board[2][0:3]
        quad0Numbers =  [s for s in quad0Numbers if s.isdigit()]
        print('quad num: ', quad0Numbers )
        quad0Needs = [possibleNums[n] for n in range(len(possibleNums)) if possibleNums[n] not in quad0Numbers]
        print('needs', quad0Needs)
 
        cube = [[[]]]
        cube[x][y][]
        

        # for i in range(9):
        #     for x in range(9):
        #        if board[i][j] == '.':
        #            # empty cell
        #            # check r/c rule
        #            cube
                   # if checkRowAndColFor():


#        for i in range(len(quad0Needs)):
#                        print("for " + quad0Numbers[i] +  ": " + checkRowAndColFor(quad0Needs[i], ))
        print(quad0Numbers) 

#        print(board1[0][0]) = 5
#        print(board1[1][0]) = 6
#        print(board1[0][1]) = 3



def checkRowAndColFor(num, x, y):
    # returns [0,0] if num not in row or col
    #         [1,0] if num in row not col
    #         [0,1] if num in col not row
    #         [1,1] if num in col and row
    ret = [0,0]
    isRow = False
    # check row
    if board[x].contains(num):
        ret = [1,0]
        isRow = True

    # check col
    for x in range(9):
        if x != int(num):
            if board[x][y] == num:
                ret = [0,1]
                if isRow:
                    ret = [1,1]
    

board1 = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
solveSudoku(board1)
#print(board1) 



