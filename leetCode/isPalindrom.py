class Solution:
	def isPalindrome(self, x: int) -> bool:
		if x<=0: # if palidrome negative
			return False
		xStr = str(x) # type cast to string
		xStrLen = len(xStr) # get length
		midIndex = xStrLen//2 - 1 # find midpoint 0 index
		if xStrLen == 1: # one number is a palindrome
			return True
		
		if xStrLen == 2: # if theres two numbers
			if xStr[0] == xStr[1]:
				return True
			else:
				return False
	
		i = midIndex


		while i>=0: # iterate from midpoint -> 0
			if xStr[i] != xStr[i+midIndex]: # if its mirrored number is not equal
				return False
			i-=1
		return True	
	#print(isPalindrome(0,121))
	
	#print(isPalindrome(0,-121))	
	#print(isPalindrome(0,10))	
	def pal(x):

		xStr = str(x) # type cast to string
		xStrLen = len(xStr) # get length

		if xStrLen == 2: # if theres two numbers
			return True if xStr[0] == xStr[1] else False
		
		if xStrLen == 3: # if theres three
			return True if xStr[0] == xStr[2] else False
		
		midIndex = xStrLen//2
		if xStrLen % 2==0: # if even adjust middle index var
			midIndex = midIndex - 1 
		
		i = midIndex
		while i >=0:
			if xStr[i] != xStr[xStrLen-i-1]:
				return False
			i-=1
		#for i in range(midIndex): # 2 -> middle
	#		if xStr[i] != xStr[xStrLen-i-1]:
#				return False
		return True
	print(pal(121)) # true
	print(pal(-121))	# false
	print(pal(10))	# false
	print(pal(0))	# true
	print(pal(1234321))	# true
	print(pal(123321))	# true 
	print(pal(113321))	# false 