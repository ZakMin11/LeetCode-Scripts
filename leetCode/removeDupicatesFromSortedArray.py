class Solution:
	# im stupid and just realized converting to set truncates repeats smh
	# all this for nothing
	def failremoveDuplicates(self, nums) -> int:
		#temp = nums[0]
		k=1
		last = nums[0]
		i=1
		while(i<len(nums)-1):
			if nums[i]>last:
				nums[k] = nums[i] 
				k+=1
				#nextIndex = i
			elif nums[i] == last:
				k+=1
			if i==len(nums)-1:
				nums[i-k:] = "_"*k 
			#else:
		#		l.append(nums[i])
				
			last = nums[i]
			i+=1	
		print(nums)
		return k
	def removeDuplicates(self, nums):
		numsLength = len(nums)
		temp = list(set(nums))
		tempLength = len(temp)
		nums = temp
		del nums[tempLength:]
		#addTemp = ["_"]*(numsLength-tempLength)
		#nums = temp + addTemp
		#temp.append(addTemp[0].split())
		#nums = temp
		print(nums)
		return tempLength
	def 
	c1 = [1,1,2]
	c2 = [0,0,1,1,1,2,2,3,3,4]
	print(removeDuplicates(0,c1))
