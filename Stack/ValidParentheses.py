class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {
            ")":"(",
            "]":"[",
            "}":"{",
            }
         
        for c in s:
            if c in brackets.values():
                stack.append(c)
            if c in brackets.keys():
                if len(stack) == 0:
                    return False
                elif brackets[c] != stack.pop():
                    return False
        return len(stack)==0

