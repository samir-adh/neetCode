

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        n = len(nums)
        max_nums = max(nums)
        min_nums = min(nums)
        tab = [[0,None]]*(max_nums-min(0,min_nums))
        visited = set()
        for i in range(n):
            if nums[i] in visited:
                tab[nums[i]-min_nums][0] +=1
            else:
                visited.add(nums[i])
                tab[nums[i]-min_nums] = [1,nums[i]]
        tab = sorted(tab)
        answer = [x[0] for x in tab]
        return answer[k:]


nums = [1,1,1,2,2,3]
k = 2
print(Solution().topKFrequent(nums=nums,k=k))