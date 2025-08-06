from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        # invert matrix
        n = len(matrix[0])
        for x in range(n):
            for y in range(n):
                if x>=y:
                    continue
                temp = matrix[x][y]
                matrix[x][y] = matrix[y][x]
                matrix[y][x] = temp
        # mirror center of x
        for x in range(n):
            y = n//2
            while y<n:
                temp = matrix[x][y]
                matrix[x][y] = matrix[x][n-y-1]
                matrix[x][n-y-1] = temp
                y+=1
    
    m = [[1,2,3],[4,5,6],[7,8,9]]        
    #m = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
    rotate(0, m)
    #print(m == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]])
    print(m==[[7,4,1],[8,5,2],[9,6,3]])
