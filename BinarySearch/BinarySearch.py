class Solution:
    def search(self, nums: list[int], target: int) -> int:
        n = len(nums)
        a = 0
        b = n-1
        if len(nums) == 1:
            return nums[0]
        while a != b:
            if nums[a] == target:
                return a
            elif nums[b] == target:
                return b
            else:
                if (b-a)//2 == 0:
                    return -1
                if target > nums[(b-a)//2]:
                    a += (b-a)//2
                else:
                    b -= (b-a)//2
        return -1


nums = [-1,0,3,5,9,12]

target = 9

sol = Solution().search(nums,target)
print(sol)