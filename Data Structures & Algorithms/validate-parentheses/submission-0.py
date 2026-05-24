class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        parenthesesMap = {"}":"{",")":"(","]":"["}

        for char in s: 
            if char in parenthesesMap.values():
                stack.append(char)
            elif char in parenthesesMap.keys():
                if not stack or parenthesesMap[char] != stack.pop():
                    return False

        return not stack