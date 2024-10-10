# Zak Mineiko
# Leet code 14. Longest Common Prefix
# easy
# Complete
# runtime: 31 ms beats 91.74% (somehow)
# memory: 16.64 MB, beats 26.23%

# strat: (unfinished)
    # loop 0 -> len
    # if occurence found in other words increment
    
# strat: (not it cheif)
        # set up dictionary
        # find longest string
        # iterate and use ptr over longest string
        # search for occurence from i->ptr in other string
        #  if occurence, save substring to dictionary key, increment num of occurences and save to dictionary value
        #  return key with largest value in dictionary
class Solution:

    # apparently best in runtime
    def LCP(self,strs)->str:
        if len(strs) == 1:
            return strs[0]
        smallestWord = min(strs,key=len)
        strs.remove(smallestWord) 
        largestPrefix=""
        for i in range(len(smallestWord)):
            i=i+1
            b = False
            for w in strs:
                if smallestWord[0:i] != w[0:i]:
                    b = True
            if not b:
                if w[0:i]>largestPrefix:
                    largestPrefix=w[0:i] 
            else:
                return largestPrefix
        return largestPrefix

    # more elegant but is worse in runtime
    def LCP(self,strs)->str:
        if len(strs) == 1:
            return strs[0]
        smallestWord = min(strs,key=len)
        strs.remove(smallestWord) 
        largestPrefix=""
        for i in range(len(smallestWord)):
            i=i+1
            b = False
            for w in strs:
                if smallestWord[0:i] != w[0:i]:
                    return largestPrefix
            if w[0:i]>largestPrefix:
                largestPrefix=w[0:i] 
        return largestPrefix
    
    #this was silly first attempt, started a type conversion idea but was headed to a dead end
    def wrongLongestCommonPrefix(self, strs) -> str:
        if len(strs)==1:
            return strs[0]
        shortestString = min(strs, key=len)

        twoList = []
        indexList = []
        count = 0
        for w in strs:
            indexList.append(count)
            count+=1
            twoList.append(w[:2])
        twoList = set(twoList)

        #print("sd", shortestString)
        l = len(shortestString)+1
        #print(l)
        strs.remove(shortestString)
        largestOccur = 0
        largestOccurStr = ""
        count = 0
        for i in range(1,l):
            subString = shortestString[0:i]
            #print(subString)
            numOccur = 0
            for word in strs:
                #print("compare",subString)
                #print("sbtring:",word[0:i])
                if subString == word[0:i]:
                    #print("found",subString, word[0:i])
                    numOccur+=1
                    count +=1
                 
            
            if numOccur >= largestOccur and numOccur!=0:
                #print("found",numOccur, largestOccur, largestOccurStr)
                largestOccur = numOccur
                largestOccurStr = subString
                #count = 0
        print(count, len(strs)+1)
        
        #return largestOccurStr if count == len(strs)+1 else ""
        return largestOccurStr
        #return occurence.index(max(k for k in occurence.values()))


    # testing
    s1= ["flower","flow","flight"] # -> fl
    s2 = ["dog","racecar","car"] # -> ""
    s3 = ["ab","a"] # -> a
    s4 = ["reflower","flow","flight"] # -> ""
    #print(longestCommonPrefix(0,s1))
    #print(longestCommonPrefix(0,s2))
    #print(longestCommonPrefix(0,s3))
    #print(longestCommonPrefix(0,s4))
    print(LCP(0,s1))
    print(LCP(0,s2))
    print(LCP(0,s3))
    print(LCP(0,s4))
    #LCP(0,s2)
    #LCP(0,s3)
