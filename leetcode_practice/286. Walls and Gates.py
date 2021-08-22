class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        m, n = len(rooms), len(rooms[0])
        gates = [(i, j) for (i, row) in enumerate(rooms) for (j, col) in enumerate(row) if not col]
        while gates:
            i, j = gates.pop(0)
            for x, y in ((i-1, j), (i+1, j), (i, j-1), (i, j+1)):
                if 0 <= x < m and 0 <= y < n and rooms[x][y] == 2**31-1:
                    rooms[x][y] = rooms[i][j] + 1
                    gates.append((x, y))
