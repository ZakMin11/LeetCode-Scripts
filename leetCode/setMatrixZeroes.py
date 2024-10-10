# Zak Mineiko
# Leetcode problem #73 Set Matrix Zeros

class Solution:
	def setZeroes(self, matrix)->None:
		# modify in place 
		# do not return anything
		#x,y
		#x = matrix[1].index(0)
		#print(x)
		for i in range(len(matrix)):
			x = matrix[i].index(0,i) if 0 in matrix[i] else None
			print(x)
			if 0 in matrix[i]:
				matrix[i] = range
				x = matrix
				y = matrix[i]	
	mat = [[1,1,1],[1,0,1],[1,1,1]]
	mat2 = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
	setZeroes(0,mat2)	
