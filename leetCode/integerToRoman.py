# Zak Mineiko
# Leet code 12. Integer to Roman
# medium
# Completed
# runtime: 67ms beats 5.15%
# memory: 16.65 MB beats 15%

# wow this code is poop. impove it
class Solution:
	def intToRoman(self, num)->str:
#If the value does not start with 4 or 9:
	#select the symbol of the maximal value that can be subtracted from the input, append that symbol to the result, subtract its value, and convert the remainder to a Roman numeral.
#If the value starts with 4 or 9:
	#use the subtractive form representing one symbol subtracted from the following symbol, for example, 4 is 1 (I) less than 5 (V): IV and 9 is 1 (I) less than 10 (X): IX. Only the following subtractive forms are used: 4 (IV), 9 (IX), 40 (XL), 90 (XC), 400 (CD) and 900 (CM).
#Only powers of 10 (I, X, C, M) can be appended consecutively at most 3 times to represent multiples of 10. You cannot append 5 (V), 50 (L), or 500 (D) multiple times. If you need to append a symbol 4 times use the subtractive form.
			# key, vlaue
			romanTable = {
				"I": 1,
				"V":5,
				"X":10,
				"L":50,
				"C":100,
				"D":500,
				"M":1000
			}	
			subtractiveForm = {
				4:"IV",
				9:"IX",
				40:"XL",
				90:"XC",
				400: "CD",
				900: "CM"
			}
			retStr = ""
			l = len(str(num)) # 4
			#modNum = l # 4
			
			for i in range(l): # 0 -> 4
				modNum = l-i-1
				number = str(num)[i]
				number = number+'0'*modNum
				#print(number)
				if int(number) in romanTable:
					retStr+= romanTable[int(number)]
					#print("romanFound: ", romanTable[int(number)], number)
				elif int(number) in subtractiveForm:
					retStr+=subtractiveForm[int(number)]
					#print("subFound: ",subtractiveForm[int(number)])
				else:
					#print("Else")
					rValues = list(romanTable.values())[::-1] # reverse list of numbers
					rKeys = list(romanTable.keys())[::-1]
					
					for i in range(len(rValues)):		
						#print(int(number),rValues[i],int(number)%rValues[i])
						if int(number)%rValues[i] == 0:
							#print(type(rValues[i]))
							#print("a",rKeys[rValues.index(rValues[i])])
							retStr=retStr+str(rKeys[rValues.index(rValues[i])])*(int(number)//rValues[i])
							number = str(int(number)-rValues[i]*(int(number)//rValues[i]))
							break
						elif int(number)>rValues[i]:
							#print("ELIF", str(rKeys[rValues.index(rValues[i])]))
							retStr+=str(rKeys[rValues.index(rValues[i])])
							number = str(int(number) - rValues[i]) 
							#print("elif number",number)
			return retStr
				

	n1 = 3749 # -> MMMDCCXLIX
	n2 = 58 # -> LVIII
	n3 = 1994 # -> MCMXCIV
	print(intToRoman(0,n1)) 
	print(intToRoman(0,n2))
	print(intToRoman(0,n3)) 

'''
CLEAN VERSION OF THE FUNCTION
def intToRoman(self, num: int) -> str:
        romanTable = {
        "I": 1,
        "V":5,
        "X":10,
        "L":50,
        "C":100,
        "D":500,
        "M":1000
        }	
        subtractiveForm = {
        4:"IV",
        9:"IX",
        40:"XL",
        90:"XC",
        400: "CD",
        900: "CM"
        }
        retStr = "" # return string
        l = len(str(num)) # length of number
        for i in range(l):
            numZeroes = l-i-1 # number of zeroes to add to number
            number = str(num)[i]
            number = number+'0'*numZeroes # add zeroes

            if int(number) in romanTable: # if number is roman numeral
                retStr+= romanTable[int(number)]
            elif int(number) in subtractiveForm: # if number is subtractive form
                retStr += subtractiveForm[int(number)]
            else:
                rValues = list(romanTable.values())[::-1] # reverse list of roman numbers
                rKeys = list(romanTable.keys())[::-1] # reverse list of roman numerals
                for i in range(len(rValues)): # loop through roman numerals
                    if int(number)%rValues[i] == 0: # if number is cleanly divisible
                        # add roman numeral the amount of times current number divides into roman number
                        retStr=retStr+str(rKeys[rValues.index(rValues[i])])*(int(number) // rValues[i])
                        # update number
                        number = str(int(number) - rValues[i]*(int(number)//rValues[i]))
                        break # break out of loop
                    elif int(number)>rValues[i]: # if a roman number can go into current number
                        # update return string with corresponding roman numeral
                        retStr+=str(rKeys[rValues.index(rValues[i])])
                        # update number subtracting current number
                        number = str(int(number) - rValues[i]) 
        return retStr



'''
