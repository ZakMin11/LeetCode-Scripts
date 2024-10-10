class Solution:
	def convert(self,s, numRows):
		# PAYPALISHIRING numRows = 4
		#P__I__N
		#A_LS_IG
		#YA_HR
		#P__I
		
		x=""
		for y in range(numRows):
			for i in range (len(s)):
				x+=s[len(x)]
				if i==y:
					print(s[len(x)]);
			
			print()
			x=""

	s = "PAYPALISHIRING"
	numRows = 4
	convert(0,s, numRows)