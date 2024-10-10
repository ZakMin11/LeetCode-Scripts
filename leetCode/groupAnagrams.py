'''
Zak Mineiko
leetcode 49. Group Anagrams
medium
inclomplete
'''


# so an anagram is a word or phrase formed by rearranging the letters of a 
# different word or phrase
# 

so the game plan:

    - order list of strs by len
    - seperate into list of same len list of strings
    - check if each str in list of lists are anagrams
        -   convert both strings to sets and check if sorted(s1==s2)
                - if yes, return true else false
    - for each same size strings
        - if yes append ret list s1, s2
    
        
class Solution:

   
	def isAnagram(self, s1, s2) -> bool:
        list(s1)
        i = 0
        seen = dict{s1[i]:1}
        while i < len(s1):
            if s1[i] is in seen:
                seen[i] += 1
        if max(seen.values()):
        # if len(s1) != len(s2):
			# return False
		# else:
			# if(sorted(s1)==sorted(s2)):
				# return True
			# else:
				# return False
	
	def groupAnagrams(self, strs) -> List[List[str]]:
        retList = [[]]
        strs = sorted(strs, key=len)
        
		for i in range(len(strs)):		
			if 
			
	s1 =["eat","tea","tan","ate","nat","bat"]
	s2 = [""]
	s3 = [["a"]] 
	print(groupAnagrams(0,s1))
	print(groupAnagrams(0,s2))
	print(groupAnagrams(0,s3))
