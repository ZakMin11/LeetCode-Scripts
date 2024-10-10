# Zak Mineiko
# Leetcode #74 Search a 2D Matrix

class Solution:
	def searchMatrix(self, matrix, target) -> bool:
		for i in range(len(matrix)):
			if matrix[i][0] < target and matrix[i][-1] > target:
				if target in matrix[i]:
					return True
		return False

	mat = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
	target = 13
	print(searchMatrix(0,mat, target))
 
