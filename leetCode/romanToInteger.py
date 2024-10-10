# Zak Mineiko
# Leet code 13. Roman to Integer
# easy
# Completed
# runtime: 54 ms, beats 19%
# memory: 16.61 MB, beats 9.25%

# fix this crappy code fr

class Solution:
    # s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M')
    def romanToInt(self, s) -> int:
        # key, value
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
				"IV":4,
				"IX":9,
				"XL":40,
				"XC":90,
				"CD":400,
				"CM":900
		}
        retInt = 0
        subFormKeys = list(subtractiveForm.keys())[::-1] # sub form numerals
        #print(subFormKeys)
        subFormValues = list(subtractiveForm.values())[::-1] # sub form numbers
        romanKeys = list(romanTable.keys())[::-1] # numerals
        romanValues = list(romanTable.values())[::-1] # numbers
        i=0
        while i <=len(s)-1:
            #print(i)
           # print(s[i:])
            #print(type(i))
            if s[i:i+2] in subFormKeys:
                #print("subfound",subFormValues[subFormKeys.index(s[i:i+2])])
                retInt+=subFormValues[subFormKeys.index(s[i:i+2])]
                i+=1
            elif s[i] in romanKeys:
                #print(" romFound",romanValues[romanKeys.index(s[i])],s[i])
                retInt+= romanValues[romanKeys.index(s[i])]
            #if i>=len(s)-1:
            #    break
            i+=1
        #print(romanValues[romanKeys.index(s[i-1])])
        #retInt+= romanValues[romanKeys.index(s[i-1])]    
        return retInt
                
        
    s1 = "III" # -> 3
    s2 = "LVIII" # -> 58
    s3 = "MCMXCIV" # -> 1994
    print(romanToInt(0,s1))
    print(romanToInt(0,s2)) 
    print(romanToInt(0,s3))


    '''
    === cleaned up function ===
    def romanToInt(self, s: str) -> int:
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
            "IV":4,
            "IX":9,
            "XL":40,
            "XC":90,
            "CD":400,
            "CM":900
        }
        retInt = 0
        subFormKeys = list(subtractiveForm.keys())[::-1] # sub form numerals
        subFormValues = list(subtractiveForm.values())[::-1] # sub form numbers
        romanKeys = list(romanTable.keys())[::-1] # numerals
        romanValues = list(romanTable.values())[::-1] # numbers
        i=0
        while i <=len(s)-1:
            if s[i:i+2] in subFormKeys: # if two chars in subtract form
                retInt+=subFormValues[subFormKeys.index(s[i:i+2])] # increment by subform value
                i+=1 # increment index
            elif s[i] in romanKeys: # else a normal roman numeral
                retInt+= romanValues[romanKeys.index(s[i])] # increment by roman numeral value
            i+=1
        return retInt
    '''