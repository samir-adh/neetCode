class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        right = n - 1
        left = 0
        while numbers[left] + numbers[right] != target:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
        return [left+1,right+1]


numbers = [2, 7, 11, 15]
target = 9
Solution().twoSum(numbers=numbers, target=target)
