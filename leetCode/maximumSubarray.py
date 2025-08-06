# Zak Mineiko
# Leet code 53. Maximum Subarray
# Medium 
# Completed Jul 30, 2025
# runtime: 86 ms beats 40 %
# memory: 31.6 MB beats 97.65%


def maxSubArray(nums):
    current = nums[0]
    maxSum = current
    for num in nums[1:]:
        current = max(num, current + num)
        maxSum = max(maxSum, current)

    return maxSum

nums1 = [-2,1,-3,4,-1,2,1,-5,4]
nums2 = [1] 
nums3 = [5,4,-1,7,8]
print(maxSubArray(nums1),maxSubArray(nums2),maxSubArray(nums3) )
