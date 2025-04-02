# TODO
class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        p = 1
        zeros_idx = []
        for i, n in enumerate(nums):
            if n == 0:
                zeros_idx.append(i)
                continue
            p *= n
        if len(zeros_idx) > 1:
            return [0] * len(nums)
        if len(zeros_idx) == 1:
            out = [0] * len(nums)
            out[zeros_idx[0]] = p
            return out
        else:
            out = nums.copy()

            for i, n in enumerate(out):
                if n == 0:
                    out[i] = p
                    continue
                out[i] = p // n
            return out


nums = [-1, 1, 0, -3, 3]
nums = [1,2,3,4,1,2,3,4,1,2,3,4]

print(Solution().productExceptSelf(nums=nums))

