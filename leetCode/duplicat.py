class Solution:
    def removeDuplicates(self, nums)->int:
        i=0
#        next = 1
        k = 0
#        isNextLetter = False
#        temp = nums[next]
        repeats = 0
        #print(nums)
        t= 0
        
        while i < len(nums)-1:  
            #print(i, len(nums)-1)
            ind = i+1
            while True and ind<len(nums)-1:
                repeats+=1
                ind+=1    
                if(nums[i] != nums[ind]):
                    break
                
            #print(t,i,nums[i], nums[ind])
            
            #if i == len(nums):
            #    nums[ind]= nums[-1]
            
            nums[t] = nums[i]
            i=ind
            t+=1
        nums[t] = nums[-1]
        del nums[t+1:]
        #print("afterLoop: ",i,ind, t, nums)
        print(nums)
        return len(nums)
    

    def cleanRD(self, nums)->int:
        #print(set(nums),len(set(nums)))
        if len(set(nums)) == 2: # if there is one repeat, return 1
            del nums[1:]
            return 1
        elif len(set(nums)) == len(nums):
            return 0
        i = 0
        t = 0
        while i < len(nums)-1:
            #ind = i+1
            while True and ind<len(nums)-1: #do while loop
                ind+=1
                if(nums[i] != nums[ind]): # while condition
                    break
            nums[t] = nums[i]
            ind = i+1
            i = ind
            t+=1
        nums[t] = nums[-1]
        del nums[t+1:]
        print(nums)
        return len(nums)        
    c1 = [0,0,1,1,1,2,2,3,3,4]
    c2 = [1,1,2 ]
    c3 = [1,2,2 ]
    c4 = [1,2,3]
    c5 = [1,1,2,2]
    print(cleanRD(0,c1)) # 5, [0,1,2,3,4]
    print(cleanRD(0,c2)) # 2, [1,2]
    print(cleanRD(0,c3)) # 2, [1,2]
    print(cleanRD(0,c4)) # 0, [1,2,3]
    print(cleanRD(0,c5)) # 2, [1,2]
    #print(removeDuplicates(0, c1))
    ##print(removeDuplicates(0, c2))
    #print(removeDuplicates(0, c3))