# Zak Mineiko  
# leet code 135. Candy
# hard

# inccomplete

class Solution:
    def candy(self, ratings) -> int:
        
        candies = len(ratings)
        
        if candies == 1:
            return 1
        
        
        if ratings[0] > ratings[1]:
            candies += 1
        i=1
        while i < candies - 2:
            print(ratings[i])
            if ratings[i] > ratings[i-1] or ratings[i] > ratings[i+1]:
                candies+=1 
            i+=1
        if ratings[len(ratings)-1] > ratings[len(ratings)-2]:
            candies += 1
        return candies


    def c(self, ratings):
        l = len(ratings)
        print(ratings[2],ratings[3],ratings[4])
        candies = l
        if candies == 1:
            return 1
        i=0
        while i < l:
            try:
                if ratings[i] > ratings[i-1] and ratings[i] > ratings[i+1]:
                    candies+=2
                elif ratings[i] > ratings[i-1] or ratings[i] > ratings[i+1]:
                    candies +=1
                    print("try",ratings[i], candies)
            except IndexError:
                if i==0:
                    if ratings[i]>ratings[i+1]:
                        candies+=1
                        print("except0",ratings[i], candies)
                elif i==l-1:
                    if ratings[l-1]>ratings[l-2]:
                        candies+=1
                        print("exceptL",ratings[i], candies)
            finally:
                i+=1
        return candies
    
    # ok i understand kinda now
    def cand(self, ratings):

        #l = [1,2,87,87,87,2,1]  
        l = [1,2,3,4,5,6,7,8,9,10,11,12,13]
        s = 1
        e = len(l)-1
        
        while s < len(l)//2:
            try:
                print(l[s-1:s+2], l[e-2:e+1]) 
            except IndexError:
                if s==0:
                    print("ss",l[s:s+1], l[e-1:e])
            finally:
                s+=1
                e-=1
            if s==len(l)//2:
                print(l[s-1:s+2])
                print(l[s],len(l)//2)
                print(l[s],l[6])
        
                
                        


    r1 = [1,0,2]
    r2 = [1,2,2]
    r3 = [1,2,87,87,87,2,1] 
    a3 = [1,2, 3, 1, 3,2,1]
    #7
    #8
    #9
    #9
    #10
    #11
    #print(candy(0, r1))
    #print(candy(0, r2))
    #print(c(0, r3))
    cand(0,0)
