'''Zak mineiko
leetcode 35. Search Insert Position
Easy
Completed Jul 30, 2025
run time: 0ms (O(nlog))
memory: 18.25 MB
'''


def searchInsert(nums, target):
	if target in nums:
            return nums.index(target)
        minimum = nums[0]
        maximum = nums[-1]
        # if there is one element
        if target > maximum:
            return len(nums)
        if target < minimum:
            return 0

        # if target goes in between 2 elements
        if len(nums) == 2:
            if target in nums:
                return nums.index(target)
            if nums[0] < target:
                return 1
        elif len(nums) == 3: # if the target goes in between 3 elements
            if target == nums[1]:
                return 1
            elif target > nums[0] and target < nums[1]:
                return 1
            else:
                return 2
        if ((maximum - target)>(target - minimum)):
            # target is closer to maximum, traverse in reverse order
            print("target closer to maximum")
            i = len(nums) - 1
            fit = i
            while i > 0:
                if nums[i] == target:
                    return i
                if nums[i-1] < target and target < nums[i]:
                    fit = i
                i-=1
            return fit
        else:
            # start from the front
            print('target closer to minimum')
            i = 0
            fit = i
            #print("min: ", nums[i:(len(nums)//2)+1])
            while i < len(nums)-1:
                print(nums[i], nums[i+1])
                if nums[i] == target:
                    return i
                if nums[i] < target and target < nums[i+1]:
                    fit = i + 1
            #      print(fit)
                i+=1
            return fit

target = 5
# nums = [1,3,5,6]
nums = [1,3,5,6] 
# nums = [1,3] 
nums = [1,3,5]
print(searchInsert(nums, 4))
# print(searchInsert(nums, 2))
# print(searchInsert(nums, 7))
