class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int] | None:
        nums_strd = sorted(nums)
        n = len(nums)
        for i in range(n):
            comp = target - nums[i]
            if comp in nums_strd and i != nums.index(comp):
                return [i, nums.index(comp)]


if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6
    res = Solution().twoSum(nums=nums, target=target)
    print(res)
