class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        left = 0
        right = 0
        hashmap = {}
        for char in s1:
            hashmap[char] = 1 + hashmap.get(char, 0)
        check = {}

        while right < len(s2):
            check[s2[right]] = 1 + check.get(s2[right], 0)

            if (right - left + 1) > len(s1):
                check[s2[left]] -= 1
                if check[s2[left]] == 0:
                    del check[s2[left]]
                left += 1

            
            if check == hashmap:
                return True
            right += 1
        return False

                
                