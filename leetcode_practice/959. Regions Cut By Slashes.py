class Solution:
    def regionsBySlashes(self, grid: List[str]) -> int:
        n = len(grid)
        parent = [i for i in range(4 * n * n)]
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(x, y):
            root_x, root_y = find(x), find(y)
            if root_x != root_y:
                parent[root_x] = root_y
        
        for i in range(n):
            for j in range(n):
                base = 4 * (i * n + j)
                char = grid[i][j]
                if char == '\\':
                    union(base + 1, base + 2)
                    union(base + 0, base + 3)
                elif char == '/':
                    union(base, base + 1)
                    union(base + 2, base + 3)
                else:
                    union(base + 1, base + 2)
                    union(base + 0, base + 3)
                    union(base, base + 2)
                if i < n - 1:
                    union(base + 3, base + 4 * n + 1)
                if j < n - 1:
                    union(base + 2, base + 4)
        
        return sum(parent[i] == i for i in range(4 * n * n))
        
            
