class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}
        for char in s:
            if char in hashmap:
                hashmap[char] += 1
            else:
                hashmap[char] = 1
        print (hashmap)
        for char in t:
            if char in hashmap:
                hashmap[char] -= 1
                if hashmap[char] == 0:
                    del (hashmap[char])
            else:
                hashmap[char] = 1

        if hashmap == {}:
            return True
        else:
            return False
