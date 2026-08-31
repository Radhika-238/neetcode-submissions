class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = {}
        for s in strs:
            charCount = [0] * 26

            for char in s:
                charCount[ord(char) - ord('a')] += 1

            key = tuple(charCount)
            if key in hashmap:
                hashmap[key].append(s)
            else:
                hashmap[key]= [s]
        return list(hashmap.values())