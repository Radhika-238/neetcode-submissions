class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left = 0
        right = 0
        hashmap = {}
        check = {}

        for char in t:
            hashmap[char] = hashmap.get(char, 0) + 1
            check[char] = 0
        
        have = 0
        need = len(hashmap)
        length = float('inf')
        

        while right < len(s):
            if s[right] in check:
                check[s[right]] += 1
                if check[s[right]] == hashmap[s[right]]:
                    have += 1

                while have == need:
                    if (right-left+1) < length:
                        result = [left, right]
                        length = (right-left+1)
                    if s[left] in check:
                        check[s[left]] -= 1
                        if check[s[left]] < hashmap[s[left]]:
                            have -= 1
                    left += 1
            right += 1
        if length != float('inf'):
            left, right = result
            return s[left:right + 1] 
        else:
            return ''

                    
                
                    




        
