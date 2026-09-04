class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i=0
        result = 0
        hashmap = {}
        for j in range (len(s)):
            if s[j] in hashmap:
                i = max(hashmap[s[j]] + 1, i)
            hashmap[s[j]] = j
            result = max(result, j-i + 1)
        return result

