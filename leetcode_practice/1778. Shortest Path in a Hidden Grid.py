# """
# This is GridMaster's API interface.
# You should not implement it, or speculate about its implementation
# """
#class GridMaster(object):
#    def canMove(self, direction: str) -> bool:
#        
#
#    def move(self, direction: str) -> bool:
#        
#
#    def isTarget(self) -> None:
#        
#

class Solution(object):
    def findShortestPath(self, master: 'GridMaster') -> int:
        dirs = {'U': (0, 1), 'D': (0, -1), 'L': (-1, 0), 'R': (1, 0)}
        antidir = {'U': 'D', 'D': 'U', 'L': 'R', 'R': 'L'}
        isValid = {}
        isValid[(0, 0)] = master.isTarget()
        
        def dfs(i, j):
            for d in dirs:
                nr, nc = i + dirs[d][0], j + dirs[d][1]
                if (nr, nc) not in isValid and master.canMove(d):
                    master.move(d)
                    isValid[(nr, nc)] = master.isTarget()
                    dfs(nr, nc)
                    master.move(antidir[d])
        
        dfs(0, 0)
        
        qu = collections.deque([(0, 0, 0)])
        seen = set()
        while qu:
            row, col, step = qu.popleft()
            if isValid[(row, col)]:
                return step
            else:
                for nr, nc in ((row + 1, col), (row - 1, col), (row, col + 1), (row, col - 1)):
                    if (nr, nc) in isValid and (nr, nc) not in seen:
                        seen.add((nr, nc))
                        qu.append((nr, nc, step + 1))
        return -1
            
                    
                    
                    
