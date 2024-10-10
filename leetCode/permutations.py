class Solution:
	def permute(self, nums):
		if len(nums)==1:
			return [nums[0]]
		retList = []
		interLength = len(nums) * 2
		for i in range(interLength):
			tempList = []
			for x in range(len(nums)):
				tempList.append(nums[x])
			retList.append(tempList)
#			temp = 
		return retList
	
	def check(nums):
		fact = 1
		for i in range(1,len(nums)):
			fact = fact*i
		return fact
#	print(permute(0,[1,2,3]))
	print(check([1,2,3]))	
