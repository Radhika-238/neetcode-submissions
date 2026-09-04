class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        allowed = k
        result = 0
        right = 0
        hashmap = {}
        max_value = 0
        
        while right < len(s):
            hashmap[s[right]] = 1+ hashmap.get(s[right], 0)
            max_value = max(max_value, hashmap[s[right]])

            if (right - left + 1) - max_value  > k:
                hashmap[s[left]]-=1
                left += 1
            result = max(result, right - left + 1)
            right += 1
        return result






                