class Solution:
    def myAtoi(self, s: str) -> int:
        isPos = True
        isReading = False
        integerString = ""
        
        for i in range(len(s)):
            print(ord(s[i]))
            if isReading and ord(s[i]) <48 or ord(s[i]) >57: # if not number and isReading
                break
            if ord(s[i]) == 45 and isReading!=True:# if neg found and not reading
                isPos = False
            if ord(s[i]) >=49 and ord(s[i]) <=57 and isReading != True: # if a number 1-9 and not reading
                isReading = True # start reading
                integerString += s[i] 
            elif isReading and ord(s[i]) >=48 and ord(s[i]) <=57: # if a number 0-9 and reading number
                integerString += s[i]    
            if integerString!='':
                if int(integerString) > 2**31-1: # if overflow in pos dir
                    integerString = str(2**31-1)
                if int(integerString) < -2**31:
                    integerString = str(-2**31)
        print(integerString, type(integerString))
        if integerString == '':
            return 0
        return int(integerString) if isPos else (-1)*int(integerString)
    s = "1337c0d3"
    s1 = "0-1"
    s2 = "words and 987"

    print(myAtoi(0,s))
    print(myAtoi(0,s1))
    print(myAtoi(0,s2))