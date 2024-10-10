'''
zak mineiko
leetcode 592. Fraction Addition and Subtraction
med



'''
 

def addFracs( fracs)-> int:
#    retFrac = {"num":0,"den":0,"isPos":True}
#j    print("------")
    total = 0
    for i in range(len(fracs["num"])):
        total= total + int(fracs["num"][i]) if int(fracs["isPos"][i]) else total-int(fracs["num"][i])
#        if fracs["isPos"][i] == False: # if negative
#             retFrac["num"] = -fracs["num"][i] + 
#        print(i)
    return total # numerator
def editFracs(fracs):
        num = fracs["num"]
        num = [int(i) for i in num]
        den = fracs["den"]
        den = [int(i) for i in den]
#        print(num)
        c = 2
        maxDen = max(den)
        maxDenInd = den.index(maxDen)
        ogMaxDen = maxDen
        i=0
        while i <len(den):
 #           print(den[i])
            #if i != maxDen:
            if maxDen%den[i]==0: # if common 
                #print("found", maxDen, den)
                print(num[i]*maxDen//den[i])
                fracs["num"][i] = str(num[i]*(maxDen//den[i])) # multiply den by max/i
                fracs["den"][i] = str(maxDen)
            else:
                #print("notFound",)
                maxDen = ogMaxDen*c
                c+=1
                i=-1
                fracs["den"][i] = str(maxDen)
            i+=1
        #print(fracs)
def reduce(num, den):
    i =num
    while i > 0:
        if den%i==0:
            return num//i, den//i
        i-=1
    return num,den
#print(reduce(36,3))
class Solution:
    def fractionAddition(self, expression)->str:
        
        fracs ={"num":[],"den":[],"isPos":[]}

        slashIndices = []
        for i in range(len(expression)):
            if expression[i] =='/':
                slashIndices.append(i)
        for i in slashIndices:
            fracs["num"].append(expression[i-1]) # numerator
            fracs["den"].append(expression[i+1]) #denominator
            fracs["isPos"].append(False if expression[i-2] == '-' else True) # sign
        
        editFracs(fracs)
        addedNum = addFracs(fracs)
        d = int(fracs["den"][0])
        if d%2==0 and addedNum%2==0 or d%2!=0 and addedNum%2!=0: #num and den even
            num, den = reduce(addedNum, d)
        else:
            num = addedNum
            den = fracs["den"][0]
        return str(num)+"/"+str(den)
        #if !(all(x == fracs["den"][0] for x in fracs["den"])): # if all den are equal
        
        #else:
    #    addFracs(fracs)   
        #print(max(fracs["den"]), all(x == fracs["den"][0] for x in fracs["den"]))
        #print(fracs) 


        #print(slashIndices)




        #print(type(expression.index('+')))
        # isNext = True
        # for i in expression:
        #     if i =='-': # if starting with neg
            
        #     elif i == '+': # if starting with positive

        #     elif i != '-' or i != '+' and isNext: # if starting and with a number
                

        #     den = 0
            # num = 0
        # while '+' in expression or '-' in expression:
        #     if '+' in 
        #     try: # positive
        #         eachNumber.append(expression[0:expression.index('+'))
        #     except: # if no positive found                  
        #         None
        #     try
                         #     print(expression[0:expression.index('+')])

    s1="-1/2+1/2"
    s2="-1/2+1/2+1/3"
    s3="1/3-1/2"
    s4 = "1/2+1/3+1/9"
    print(fractionAddition(0,s1))
#    print(fractionAddition(0,s2))
#    print(fractionAddition(0,s3))
 #   print(fractionAddition(0,s4))
