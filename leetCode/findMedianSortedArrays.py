# done
class Solution:
    def findMedianSortedArrays(self, nums1, nums2) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        nums1 = sorted(nums1 + nums2)
        fullLen = len(nums1)
        if fullLen %2==0: # even
            return float((nums1[fullLen//2]+nums1[fullLen//2 - 1])/2)
        else:
            return float(nums1[fullLen//2])
        
    nums1= [1,2]
    nums2 = [3,4]
    print(findMedianSortedArrays(0,nums1,nums2))
