# TODO
class Solution:
    def productExceptSelf(self, nums: list[int]) ->list[int]:
        length=len(nums)
        sol=[1]*length
        pre = 1
        post = 1
        for i in range(length):
            sol[i] *= pre
            pre = pre*nums[i]
            sol[length-i-1] *= post
            post = post*nums[length-i-1]
        return(sol)

nums = [-1,1,0,-3,3]

print(Solution().productExceptSelf(nums=nums))

# nums = [1,2,3,4,1,2,3,4,1,2,3,4]