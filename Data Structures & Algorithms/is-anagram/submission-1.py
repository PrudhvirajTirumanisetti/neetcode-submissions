class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # return sorted(s)==sorted(t)
        hashMapS = defaultdict(int)
        hashMapT = defaultdict(int)
        for letter in s:
            hashMapS[letter]+=1
        for letter in t:
            hashMapT[letter]+=1
        return hashMapT == hashMapS


        