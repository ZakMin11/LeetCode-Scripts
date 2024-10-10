'''Zak mineiko
leetcode 3. Longest Subtring Without Repeating Characters
medium
incomplete
run time:
memory:
'''

def lengthOfLongestSubstring(s):
	sLen = len(s)
	if sLen == 1:
		return 1
	elif sLen == 2:
		return 2 if s[0]!=s[1] else 1
	longest = ""
	for start in range(len(s)):
		temp = ""	
		word = s[start:]
		print(word)
		for l in word:			
			if l not in temp: # if letter is not in temp var
				temp = temp + l # add letter
				#	print("t:",temp)
			else:
				if len(temp)>len(longest): # if letter is in temp, check if 
					#print(temp, longest)
					longest = temp
				temp = ""
			if len(temp)>len(longest): # if letter is in temp, check if 
					#print(temp, longest)
					longest = temp
	
	return len(longest)

s1= "pwwkew" # 3 'kew'
s2="abcabcbb" # 3 'abc'
s3="bbbbb" # 1 'b'
s4 = "jbpnbwwd" # 4 'jbpn' 
s5 = "au" # 2 'au'
s6 = "cdd" # 2 'cd'	   
print(lengthOfLongestSubstring(s1))
print(lengthOfLongestSubstring(s2))
print(lengthOfLongestSubstring(s3))
print(lengthOfLongestSubstring(s4))
print(lengthOfLongestSubstring(s5))
print(lengthOfLongestSubstring(s6))