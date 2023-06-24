class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        set_nums = set(nums)
        max_count = 0
        for i in set_nums:
            count = 0
            if i - 1 not in set_nums:
                count +=1
                n = i + 1
                while n in set_nums:
                    count+=1
                    n += 1
                max_count = max(max_count,count)
            else:
                continue
        return max_count


nums = []

sol = Solution().longestConsecutive(nums=nums)
print(sol)
