class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for index, height in enumerate(heights):
            start = index
            while stack and stack[-1][1]> height:
                i,h = stack.pop()
                maxArea = max( maxArea, h*(index-i))
                start = i
            stack.append((start,height))
        
        while stack: 
            i,h = stack.pop()
            w = len(heights)-i
            maxArea = max(maxArea, h*w)
        return maxArea