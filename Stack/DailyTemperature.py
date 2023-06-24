class Solution:
    def dailyTemperatures(self, temperatures: list[int]) -> list[int]:
        length = len(temperatures)
        days_and_temperatures = [x for x in enumerate(temperatures)]
        stack = [days_and_temperatures[0]]
        answer = [0] * length
        for i in range(1, length):
            while stack and days_and_temperatures[i][1] > stack[-1][1]:
                elt = stack.pop()
                answer[elt[0]] = i - elt[0]
            stack.append(days_and_temperatures[i])
        return answer


temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
answer = Solution().dailyTemperatures(temperatures=temperatures)
print(answer)
