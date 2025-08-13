class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) <= 1:
            return len(s)
        start = 0
        end = 0
        max_length = 0
        max_freq = 0
        char_map = {}
        for end in range(len(s)):
            c = s[end]
            char_map[c] = char_map.get(c, 0) + 1
            max_freq = max(max_freq, char_map[c])
            if (end - start + 1) - max_freq > k:
                char_map[s[start]] -= 1
                start += 1
            max_length = max(max_length, end - start + 1)
        return max_length


def test_cases():
    cases = [
        # (("ABAB", 2), 4),
        # (("AABABBAA", 1), 4),
        (("ABCDAA", 2), 4),
        (("ABABABAB", 1), 5),
        (("AABBCCDD", 3), 6),
        (("AAABC", 1), 5),
    ]
    for case in cases:
        s, k = case[0][0], case[0][1]
        out = Solution().characterReplacement(s, k)
        expected = case[1]
        # assert out == expected


if __name__ == "__main__":
    test_cases()
