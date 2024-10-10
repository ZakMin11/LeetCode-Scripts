def findTwoSortedArrays(nums1, nums2):
    n = nums1+nums2
    print(n, len(n))
    print(n[len(n)//2], n[(len(n)//2)-1],n[len(n)//2] + n[(len(n)//2)-1])
    if len(n) % 2 == 0: 
        return ((n[len(n)//2] + n[(len(n)//2)-1]) / 2) 

    return n[(len(n)-1//2)-1]

#print(findTwoSortedArrays([1,2], [3,4]))
#print(findTwoSortedArrays([1,3], [2]))
print(findTwoSortedArrays([0,0,0,0,0],[-1,0,0,0,0,0,1]))