class Solution:
    def minWindow(self, s: str, t: str) -> str:
        hashMapT = defaultdict(int)
        for char in t:
            hashMapT[char]+=1

        hashMapS = defaultdict(int)
        left = 0
        have = 0 
        need = len(hashMapT)
        minWindow = [-1, -1]
        minWinLen = float("infinity")
        for right in range(len(s)):
            char = s[right]
            hashMapS[char]+=1

            if char in hashMapT and hashMapT[char] ==hashMapS[char]:
                have +=1
            
            while have == need:
                currLength = right-left+1
                if minWinLen > currLength:
                    minWinLen = right-left+1
                    minWindow = [left, right]
                hashMapS[s[left]]-=1
                char = s[left]
                if char in hashMapT and hashMapS[char] < hashMapT[char]:
                    have -=1 
                left +=1
        l, r = minWindow
        return s[l:r+1] if minWinLen != float("infinity") else ""