class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        end = 0
        max_length = 0
        char_map = {}
        while end < len(s):
            c = s[end]
            if c not in char_map.keys() or char_map[c] < start:
                char_map[c] = end
            else:
                max_length = max(max_length, end - start)
                start = char_map[c] + 1
                char_map[c] = end
            end += 1
        max_length = max(max_length, end - start)
        return max_length


# Test cases
def test_1():
    s = "abcabcbb"
    anwser = 3
    out = Solution().lengthOfLongestSubstring(s)
    assert out == anwser


def test_2():
    s = "bbbbb"
    anwser = 1
    out = Solution().lengthOfLongestSubstring(s)
    assert out == anwser


def test_3():
    s = "pwwkew"
    anwser = 3
    out = Solution().lengthOfLongestSubstring(s)
    assert out == anwser


def test_4():
    s = "aab"
    anwser = 2
    out = Solution().lengthOfLongestSubstring(s)
    assert out == anwser


def test_5():
    s = "dvdf"
    anwser = 3
    out = Solution().lengthOfLongestSubstring(s)
    assert out == anwser

def test_6():
    s = "abba"
    anwser = 2
    out = Solution().lengthOfLongestSubstring(s)
    assert out == anwser


if __name__ == "__main__":
    test_6()