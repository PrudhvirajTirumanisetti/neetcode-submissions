class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxCharFrequency = defaultdict(int) # use default dict so we dont run into key errors.
        maxLongestSubArrayLength = 0
        
        leftPointer = 0 
        for rightPointer in range(len(s)):
            maxCharFrequency[s[rightPointer]]+=1
            maxFreqValue = max(maxCharFrequency.values())
            currLength = rightPointer-leftPointer+1
            if currLength - maxFreqValue > k:
                maxCharFrequency[s[leftPointer]]-=1
                leftPointer+=1
            maxLongestSubArrayLength = max(maxLongestSubArrayLength, rightPointer-leftPointer+1)
        return maxLongestSubArrayLength