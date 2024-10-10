

'''
zak mineiko

leetcode 1905. Count Sub Islands

incomplete
'''

I want to do a O(2N^2) approach, filter islands horizontally then scan vertically to form the islands

>[...]
 [...]
 [...]

 .[..>]
 .[...]
 .[...]

class Solution:

    def countSubIslands(self, grid1,grid2)->int:
        l = len(grid1)
        ly = len(l[0])
        for x in range(l):
            for y in range(ly):
                if grid1[x][y] == grid2[x][y] and grid2[x][y]==1:





    g1 = [[1,1,1,0,0],[0,1,1,1,1],[0,0,0,0,0],[1,0,0,0,0],[1,1,0,1,1]]
    g2 = [[1,1,1,0,0],[0,0,1,1,1],[0,1,0,0,0],[1,0,1,1,0],[0,1,0,1,0]]
    g11 = [[1,0,1,0,1],[1,1,1,1,1],[0,0,0,0,0],[1,1,1,1,1],[1,0,1,0,1]]
    g22 = [[0,0,0,0,0],[1,1,1,1,1],[0,1,0,1,0],[0,1,0,1,0],[1,0,0,0,1]]
    countSubIslands(0,g1,g2)
