class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s_to_list = []
        for c in s:
            if c.isalnum():
                s_to_list.append(c)
        left = 0
        right = len(s_to_list)-1
        while left < right:
            if s_to_list[left] != s_to_list[right]:
                return False
            else:
                left += 1
                right -= 1
        return True
s = "A man, a plan, a canal: Panama"
print(Solution().isPalindrome(s))