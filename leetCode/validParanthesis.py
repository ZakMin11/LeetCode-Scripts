''' Zak Mineiko
leetcode 20. Valid Paranthesis
easy
incomplete
runtime:
memory:
'''

class Solution:
    def isValid(self, s) -> bool:
        pStack = []
        cStack = []
        bStack = []
        for i in range(len(s)):
            l = s[i]
        
            if l == "(":
                pStack.append("(")
            elif l ==")":
                try:
                    pStack.pop()
                except IndexError:
                    return False
            elif l =="{":
                cStack.append("{")
            elif l =="}":
                try:
                    cStack.pop()
                except IndexError:
                    return False
            elif l =="[":
                bStack.append("[")
            elif l =="]":
                try:
                    bStack.pop()
                except IndexError:
                    return False
            else:
                None
        fullStack = pStack+cStack+bStack
        print(fullStack)
        return True if len(fullStack) == 0 else False
        #return True if pStack+cStack+bStack)
        
        #print(",",l)
        print(len(l), "ss   ")

    s1 = "()"
    s2 = "()[]{}"
    s3 = "(])"
    s4 = "([)]"
    #print(isValid(0,s1))
    #print(isValid(0,s2))
    #print(isValid(0,s3))
    print(isValid(0,s4))
                
                
