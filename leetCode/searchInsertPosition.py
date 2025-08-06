'''Zak mineiko
leetcode 35. Search Insert Position
Easy
incomplete
run time:
memory:
'''


def searchInsert(nums, target):
    minimum = nums[0]
    maximum = nums[-1]
    if target > maximum:
        return len(nums) 
    if target < minimum: 
        return 0
# print(minimum, maximum)
    if len(nums) == 2:
        print(nums[0], nums[1])

        if nums[0] < target:
            return 1

    if ((maximum - target)>(target - minimum)):
        # target is closer to maximum, start on right half of the list
        i = (len(nums)//2-1)
        fit = i
        print(nums[i:])
        
        while i < len(nums):
            
            print("amxxx: ", nums[i], "  two: ", nums[i-1], nums[i], target)
            if nums[i] == target:
                return i
            if nums[i-1] < target and target < nums[i]:
                fit = i
          #      print("max fit: ", fit)
            i+=1
        return fit
    else:
#        print(i, (len(nums)//2)+1, nums[])
        i = 1
        fit = i
        print("min: ", nums[i:(len(nums)//2)+1])
        while i < (len(nums)//2)+2:
            print(nums[i])
            if nums[i-1] == target:
                return i
            print(nums[i-1], nums[i])
            if nums[i-1] < target and target < nums[i]:
                fit = i
          #      print(fit)
            i+=1
        return fit


target = 5
# nums = [1,3,5,6]
# nums = [1,3,5,6] 
nums = [1,3] 
nums = [1,3,5]
print(searchInsert(nums, 4))
# print(searchInsert(nums, 2))
# print(searchInsert(nums, 7))
