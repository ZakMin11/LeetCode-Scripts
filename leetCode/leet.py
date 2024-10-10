def romanToInt( s: str) -> int:
        d = {
            'I':1, 
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000
            }

        lis = []
        for l in range(len(s)):
            if s[l] in d.keys():
                lis.append(d[s[l]])
                #print(d[s[l]]) 
        su = []
        ind = 1
        for n in lis:
            if ind < len(lis):
                if 5 == int((lis[ind]/n)) or 10 == int((lis[ind]/n)):
                    su.append(lis[ind]-n)
                else:
                    su.append(n)
            else:
                su.append(n)
            ind+=1
            #print(su)
        return sum(su)
print(romanToInt("IVI"))