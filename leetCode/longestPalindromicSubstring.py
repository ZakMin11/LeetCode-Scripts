# Zak Mineiko
# leetcode 5. Longest Palindromic substring
def isPal(x):
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
	return True

class Solution:
				
	def longestPalindrome(self, s) -> str:
		longestPal = ""
		sLen = len(s)
		if sLen == 1:
			return s
		elif sLen == 2:
			if s[0] == s[1]:
				return s
			else:
				return s[0]
		#mp = sLen//2 - 1 if (sLen%2==0) else sLen//2
		x = 2
		while x< sLen: 
			#print(x)
			for i in range(sLen):
				print(" start:", i, "End:", i+x, "s: ",s[i:i+x+1])
				print(isPal(s[i:i+x]), len(s[i:i+x+1])>len(longestPal))
			#	print(i)
				if isPal(s[i:i+x+1]) and len(s[i:i+x+1])>len(longestPal):
					longestPal = s[i:i+x+1]
					print("found", longestPal)
			x+=1
		return longestPal
	def r(self,s):
		if isPal(s):
			return s
		longest = ""
		l = len(s)
		for i in range(l):
			for j in range(l):
				subs = s[i:i+j]
				if (isPal(subs)):
					if len(subs)> len(longest):
						longest = subs
						print(longest)

				#print(s[i:i+j])
		return longest
	def t(self,s):
		sLen = len(s)
		longest = ""
		print(sLen)
		#mp = sLen//2-1 if (sLen%2==0) else sLen//2
		if (sLen%2==0): # even [0,1,#,3,4,5]

			mp = (sLen//2)
			i = mp
			counter = 0

			
			while(i >= 1): # [0,1,<,3,4,5]
				# [0,1,2,3,<,5,6,7,8]
				# [0,1,2,3,i,5,6,7,8]
				# [0,1,2,i,i-1,5,6,7,8]
				# [0,1,i,i-1,i-2,5,6,7,8]
				# [0,i,i-1,i-2,i-3,5,6,7,8]
				# [i,i-1,i-2,i-3,i-4,5,6,7,8]
				#print("i: ",i)
				#print("mp: ",mp, s[0:i])
				r = s[i:mp+i-counter] # [0,1,2,#,>,>]
				#print("{{",s[0:mp],r)
				print("if: ",s[0:i],r[::-1])
				if s[0:i] == r[::-1]: #if [0,1,2]==[5,4,3]
					temp = s[0:mp+i-counter]
					#print(temp,i)
					#print("Found: ", s[0:mp+1+i])
					if len(temp) > len(longest):
						longest = temp
				i-=1
				counter+=1
			return longest
		else:
			print("hello")
			#mp = sLen//2
			#i = mp
			#while(i<=0):


		#print("mp: ", mp)
		#i=mp
		#longest = ""
		#while i>=0:
			#if odd:
				#left = s[mp-i] 
			
		#	left = s[mp-i:mp]
	#		right = s[mp:mp+i]
#			backwards = right[::-1]
			#print(left, right)
			#print(i)
			#print(s[mp-i:mp], " == ",s[mp:mp+i])
			
			#print(i, sLen-i-1)
			#print(mp,i, sLen-i, sLen-mp+i)
			#print(s[mp-i:mp+i])
			#secondHalf = s[mp:sLen-i-1]
			#print(s[i:mp], secondHalf[::-1])
			#if s[i:mp] == secondHalf[::-1]:
		#		if len(s[i:sLen-i-1])>len(longest):
	#				longest = s[i:sLen-i-1]
			
		#return longest
#		print(s[::-1])
	#sdef recur(s):

	s1="adccda" # 6, mp = 3 (len//2-1)
	s2="abcba" # 5, mp = 3 (len//2)
	s3="xyuuyjkluz" # 
	#s = "abcdcba"
	print(t(0,s3))
	#print(t(0,s2))
	#print(longestPalindrome(0,s))
	#print(r(0,s))
#	print(isPal(0,"abcddcba"))	
