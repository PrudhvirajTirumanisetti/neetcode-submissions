class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        Row, Col = len(heights), len(heights[0])
        pacificFlow, altanticFlow = set(), set()

        def dfs(r, c, visited, prevHeight):
            if r<0 or c< 0 or r>=Row or c>=Col or prevHeight>heights[r][c] or (r,c) in visited:
                return 
            visited.add((r,c))
            dfs(r+1, c, visited, heights[r][c])
            dfs(r-1, c, visited, heights[r][c])
            dfs(r, c+1, visited, heights[r][c])
            dfs(r, c-1, visited, heights[r][c])

        for c in range(Col):
            dfs(0, c, pacificFlow, heights[0][c])
            dfs(Row-1, c, altanticFlow, heights[Row-1][c])
        for r in range(Row):
            dfs(r, 0, pacificFlow, heights[r][0])
            dfs(r, Col-1, altanticFlow, heights[r][Col-1])

        result = []
        for r in range(Row):
            for c in range(Col):
                if (r,c) in pacificFlow and (r,c) in altanticFlow:
                    result.append([r,c])

        return result