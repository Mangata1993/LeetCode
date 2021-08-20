class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
    # BFS
        m, n = len(grid), len(grid[0])
        queue = collections.deque()
        count = 0
        
        def bfs(queue):
            while queue:
                i, j = queue.popleft()
                for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if 0 <= i < m and 0 <= j < n and grid[x][y] == '1':
                        queue.append((x, y))
                        grid[x][y] = '2'
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # grid[i][j] = '2'
                    queue.append((i, j))
                    bfs(queue)
                    count += 1
                    
        return count
            
        
        
           
 # DFS       
        if not grid:
            return 0
        count = 0
        m = len(grid)
        n = len(grid[0])
        
        def dfs(i, j):
            if not 0 <= i < m or not 0 <= j < n or grid[i][j] != '1':
                return
            grid[i][j] = '2'
            for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                dfs(x, y)
                
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    dfs(i, j)
                    count += 1
        return count
    
    
