class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        
        s = s.replace(' ', '')
        s= s.lower()
        right = len(s) - 1
        

        while left < right:
            if not s[left].isalnum():
                print(s[left])
                left += 1
                continue
            if not s[right].isalnum():
                print(s[right])
                right -= 1
                continue
            if s[left] == s[right]:
                left += 1
                right -= 1
            else:
                return False
        return True