class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: int(a / b),
        }
        res = 0
        for t in tokens:
            if t in operators:
                b = stack.pop()
                a = stack.pop()
                stack.append(operators[t](a, b))
            else:
                stack.append(int(t))
        return stack[0]


if __name__ == "__main__":
    tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]  # 5 + (17 * ( /
    sol = Solution().evalRPN(tokens)
    print(sol)
