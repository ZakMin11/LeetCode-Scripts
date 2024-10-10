
def longest_substring(s):
    firstGo = True
    odd  = True
    sub = ""
    high = 0

    for i in range(len(s)-1):
        #if i == len(s)-1:


        if firstGo:
            if int(s[i])%2 == 0 and int(s[i+1])%2!=0:
                sub += s[i]
                odd = True
                firstGo = False
            elif int(s[i])%2 != 0 and int(s[i+1])%2==0:
                sub+=s[i]
                odd = False
                firstGo = False
        else:
            if odd is True:
                if int(s[i+1])%2==0:
                    sub += s[i+1]
                    odd = False
                    if len(sub)>high:
                        high = len(sub)
                else:
                    sub = ""
            else:
                if int(s[i+1])%2!=0:
                    sub += s[i+1]
                    odd = True
                    if len(sub)>high:
                        high = len(sub)
                else:
                    sub = ""
    return sub



        



s = "225424272163254474441338664823"
print(longest_substring(s))


#print(longest_substring("225424272163254474441338664823") == "272163254")
#print(longest_substring("594127169973391692147228678476") == "16921472")
#print(longest_substring("721449827599186159274227324466") == "7214")
