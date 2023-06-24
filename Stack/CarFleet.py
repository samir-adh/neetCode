class Solution:
    def carFleet(self, target: int, position: list[int], speed: list[int]) -> int:
        def calculate_arrival_time(position,speed):
            return (target-position)/speed
        n = len(position)
        convoy = [(position[i],speed[i]) for i in range(n)]
        convoy.sort(key=lambda x:x[0],reverse=True)
        if n < 2:
            return 1
        stack = [calculate_arrival_time(convoy[0][0],convoy[0][1])]
        for i in range(1,n):
            t = calculate_arrival_time(convoy[i][0],convoy[i][1])
            if t > stack[-1]:
                stack.append(t)
        return len(stack)

