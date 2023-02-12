class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(a: int, b: int): #call when 1 is found
            n = len(grid)
            m = len(grid[0])
            q = deque()
            q.append([a,b])
            
            dirv = [[1,0],[0,1],[-1,0],[0,-1]]
            ret = []
            while q:
                i,j = q.popleft()
                
                for x, y in dirv:
                    newi = i + x
                    newj = j + y
                    if min(newi, newj) >= 0 and newi < n and newj < m and grid[newi][newj] == '1':
                        q.append([newi,newj])
                        grid[newi][newj] = '0'

        
        ans = 0
        
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == '1':
                    grid[i][j] == '0'
                    bfs(i,j)
                    ans +=1
        return ans
                