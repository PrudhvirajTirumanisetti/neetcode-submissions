class Solution:
    def isPalindrome(self, s: str) -> bool:
        # return s==s[::-1]
        # newString = ""
        # for char in s:
        #     if char.isalnum():
        #         newString+=char.lower()
        # return newString == newString[::-1]
        # left, right = 0, len(s)-1
        # while left< right:
        #     while left < right and not s[left].isalnum():
        #         left+=1
        #     while left < right and not s[right].isalnum():
        #         right-=1
        #     if s[left].lower() != s[right].lower():
        #         return False
        #     left+=1
        #     right-=1
        # return True        
        newString = ""
        for char in s:
            if char.isalnum():
                newString+=char.lower()
        left, right = 0, len(newString)-1
        while left < right: 
            if newString[left]!=newString[right]:
                return False
            left+=1
            right-=1
        return True