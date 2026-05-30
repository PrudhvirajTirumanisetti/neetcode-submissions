class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:         
        if not s or len(s) ==1: return len(s)
        
        maxSubStringLength = 0
        charHashSet = set()

        leftPointer = 0
        for rightPointer in range(len(s)):
            while s[rightPointer] in charHashSet:
                charHashSet.remove(s[leftPointer])
                leftPointer+=1
            charHashSet.add(s[rightPointer])
            maxSubStringLength = max( maxSubStringLength, rightPointer-leftPointer+1)
        return maxSubStringLength