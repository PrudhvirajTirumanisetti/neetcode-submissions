class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        Row, Col = len(grid), len(grid[0])
        numberOfIslands = 0
        
        def dfs(r, c):
            if r <0 or r>=Row or c<0 or c>=Col or grid[r][c] !="1":
                return 
            else: 
                grid[r][c] = "0"
                dfs(r+1, c)
                dfs(r-1, c)
                dfs(r, c+1)
                dfs(r, c-1)

        for r in range(Row):
            for c in range(Col):
                if grid[r][c] == "1":
                    numberOfIslands +=1
                    dfs(r,c)
        return numberOfIslands
        