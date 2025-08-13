class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def occurence_map(word: str):
            char_map = {}
            for c in word:
                char_map[c] = char_map.get(c, 0) + 1
            return char_map

        if len(s1) == 0:
            return True
        if len(s2) == 0:
            return False
        char_map = occurence_map(s1)
        start = 0
        end = 0
        while end <= len(s2):
            window = s2[start:end]
            window_occmap = occurence_map(window)
            # print(window_occmap) 
            if char_map == window_occmap:
                return True
            if (end - start) == len(s1):
                start += 1
            end += 1
        return False


def test_solution():
    test_cases = [
        ("ab", "eidbaooo", True),
        ("eidbaooo", "ab", False),
        ("hello", "ooolleoooleh", False),
        ("adc", "dcda", True),
    ]
    for i, case in enumerate(test_cases):
        s1, s2, expected = case
        assert expected == Solution().checkInclusion(s1, s2), f"Test case {i+1} failed"

if __name__=="__main__":
    test_solution()