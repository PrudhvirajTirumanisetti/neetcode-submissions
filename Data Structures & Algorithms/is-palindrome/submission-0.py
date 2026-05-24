class Solution:
    def isPalindrome(self, s: str) -> bool:
        # return s==s[::-1]
        newString = ""
        for char in s:
            if char.isalnum():
                newString+=char.lower()
        return newString == newString[::-1]
                
        