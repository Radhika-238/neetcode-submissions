class Solution:

    def encode(self, strs: List[str]) -> str:
        delimiter = '#'
        encoded_text = ''
        for s in strs:
            length = len(s)
            encoded_text = encoded_text + str(length) + delimiter + s
        return encoded_text

    def decode(self, s: str) -> List[str]:
        result = []
        i=0
        while i < len(s):
            j=i
            while s[j] != '#' :
                j+=1
            length = int(s[i:j])
            i=j +1
            j = i+length
            word = s[i:j]
            result.append(word)
            i=j
        return result
