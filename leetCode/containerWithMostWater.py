class Solution:
    def maxArea(self, height) -> int:
        max = 0
        n = len(height)
        for i in range(n):
            ptr = i+1
            while ptr!=n:
                y = min(height[i],height[ptr])
                x = ptr-i
                if x*y > max:
                    print(height[i],height[ptr])
                    max = x*y
                ptr+=1
        return max
    h1 = [1,8,6,2,5,4,8,3,7]
    h2 = [1,1]
    print(maxArea(0,h1))
    print(maxArea(0,h2))