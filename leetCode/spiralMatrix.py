'''Zak mineiko
leetcode 54. Spiral Matrix
Medium
Completed on Jul 30, 2025 
run time: 0ms, Beats 100%
memory: 17.75 MB, beats 61.93%
'''
'''
approach:
    I am thinking of appending an empty list with just the first row, 
    then rotating the remaining matrix without the first row until 
    the last number of the second row of the matrix is at the start 
    of the new matrix then append that new second row and repeat the 
    process until the matrix is empty.
'''
def spiralOrder(matrix):
        def rotateMatrix(mat):
            rotated = list(zip(*mat))[::-1]
            m = []
            for i in rotated:
                m.append(list(i))
            return m
        
        retList = []
        # append first row to return list
        while len(matrix)!=1:
            retList.extend(matrix[0][0:])
            matrix = matrix[1:]
            matrix = rotateMatrix(matrix)
        retList.extend(matrix[0])
        return retList


matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
matrix = [[1,2,3],[4,5,6],[7,8,9]]
print(spiralOrder(matrix))
