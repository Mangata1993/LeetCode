class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        def canWalk(day):
            grid = [[0] * col for _ in range(row)]
            
            for i in range(day):
                r, c = cells[i]
                grid[r-1][c-1] = 1
            
            queue = collections.deque()
            for c in range(col):
                if grid[0][c] == 0:
                    queue.append((0, c))
                    grid[0][c] = 1
            
            while queue:
                r, c = queue.popleft()
                if r == row - 1:
                    return True
                for x, y in ((r+1, c), (r-1,c), (r, c+1), (r, c-1)):
                    if not 0 <= x < row or not 0 <= y < col or grid[x][y] == 1:
                        continue
                    grid[x][y] = 1
                    queue.append((x, y))
            return False
                    
        
        left, right = 1, len(cells) 
        while left <= right:
            mid = (left + right) // 2
            if canWalk(mid):
                left = mid + 1
            else:
                right = mid - 1
        return right
        
