class Solution:
	def mostWater(l1, weights):
		pointer = 0
		for i in range(l1):

			for j in range(l1):
				if weights[i]*j-i>biggest:
					biggest = [weights[i],]