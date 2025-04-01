

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        count = {}
        for item in nums:
            if item in count.keys():
                count[item] += 1
            else :
                count[item] = 1
        top = sorted(count.items(),key = lambda x : x[1])
        return [item[0] for item in top[-k:]]


nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent(nums=nums,k=k))