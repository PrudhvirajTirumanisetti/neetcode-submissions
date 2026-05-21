class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            encoded+=str(len(word))+"$"+word
        return encoded

    def decode(self, s: str) -> List[str]:
        decoded = [] #input = 5$Hello5$World
        i = 0
        while i < len(s):
            j = i
            while s[j] != "$":
                j+=1
            length = int(s[i:j]) # could be double digit
            decoded.append(s[j+1:j+1+length])
            i = j+1+length
        return decoded