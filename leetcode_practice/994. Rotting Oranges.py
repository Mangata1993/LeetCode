class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        count = 0
        queue = collections.deque([])
        fresh = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1
        while queue:
            for _ in range(len(queue)):
                i, j = queue.popleft()
                for r, c in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -= 1
                        queue.append((r, c))
            count += 1
        return max(0, count - 1) if fresh == 0 else -1
  
