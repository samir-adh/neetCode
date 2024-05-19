class Solution:
    def maxArea(self, height: list[int]) -> int:
        def area(left,right):
            return (right-left) * min(height[left],height[right])
        n = len(height)
        left = 0
        right = n-1
        max_height = 0
        while left < right:
            current_height = area(left=left,right=right)
            max_height = max(current_height,max_height)
            if height[left] < height[right]:
                left+=1
            else:
                right-=1
        return max_height
    
height = [1,3,2,5,25,24,5]
Solution().maxArea(height)