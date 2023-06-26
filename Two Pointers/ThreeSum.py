class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        n = len(nums)
        nums.sort()
        answer = []
        for i in range(n):
            if nums[i] > 0:
                break
            # if nums[i] == nums[i-1]:
            #     continue
            left = i+1
            right = n - 1
            while left < right:
                s = nums[left] + nums[right] + nums[i]
                if s < 0:
                    left += 1
                elif s > 0:
                    right -= 1
                elif s == 0:
                    res = [nums[left], nums[right], nums[i]]
                    if res not in answer:
                        answer.append(res)
                    left+=1
                    right-=1
                    while nums[left] == nums [left-1] and left < right:
                        left+=1
        return answer

nums = [-1,0,1,2,-1,-4]
sol = Solution().threeSum(nums=nums)
print(sol)