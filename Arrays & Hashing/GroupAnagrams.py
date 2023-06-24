class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        anagrams = []
        srtd_strs = []
        n = len(strs)
        for i,word in enumerate(strs):
            srtd_strs.append((''.join(sorted(word)),word))
        srtd_strs = sorted(srtd_strs)
        anagrams.append([srtd_strs[0][1]])
        for i in range(1,n):
            if srtd_strs[i][0] == srtd_strs[i-1][0]:
               anagrams[-1].append(srtd_strs[i][1])
            else:
                anagrams.append([srtd_strs[i][1]])
        return anagrams
    
if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    anagrams = Solution().groupAnagrams(strs=strs)
    print(anagrams)
