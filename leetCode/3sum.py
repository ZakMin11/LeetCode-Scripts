

# ok so i think we might need to do recursion
# idk tho
# maybe there is a way to cut off a bunch of fat
# by finding the median or ave or something

# you must have negative numbers to cancel out the positives
# so check if sorted list starts with negative numbers and if it ends with positive numbers
# start as close to zero as possible and work outwards
# dont know how to stop/trim more fat tho


class Solution:
    def threeSum(self, nums):
        retList = []
        l = len(nums)
        for x in range(0,l-2,4):
            for y in range(x+ 1, l-1):
                for z in range(x+2,l):
                    print(x,y,z)
                    temp = []
                    if nums[x]+nums[y]+nums[z]==0 and y!=z:
                        print(x,y,z, "!")
                    #    temp = sorted([nums[x],nums[y],nums[z]])
                        retList.append([nums[x],nums[y],nums[z]]) 
        #retset =set(tuple(i) for i in retList)
        #retList = list(list(i)for i in retset)
        
        return retList
        #print(set(retList))
        #for i in range(len(retList)):
        #    temp = retList[i].sort()
        #    print(temp)
         #   if temp in retList:
         #       retList.remove(temp)
        #    temp=[]
    def ts(self,nums):
        retList = []
        l = len(nums)
        x = 0
        for y in range(x+ 1, l-1):
            for z in range(x+2,l):
                print(x,y,z)
                temp = []
                if nums[x]+nums[y]+nums[z]==0 and y!=z:
                
                    temp = sorted([nums[x],nums[y],nums[z]])
                    retList.append(temp)
        return retList
    
    def median(nums):
        n = len(nums)
        s = sorted(nums)
        ret = (s[n//2-1]/2.0+s[n//2]/2.0, s[n//2])[n % 2]
        print(ret)
        


    def tryThis(self,nums):
        l = len(nums)
        nums.sort()
        sum = 0
        for i in range(l):
            sum += nums[i] 
        ave = sum/l

        print(ave)
    nums = [-1,0,1,2,-1,-4]
    #nums = [1,2,-2,-1]
    n = [1,2,3,4,5,6]
    #print(tryThis(0,nums))
    print(median(n))
    #print(threeSum(0,nums))

    #print(ts(0,nums))
    #print(threeSum(0,n))