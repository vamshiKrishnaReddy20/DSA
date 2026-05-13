class Solution:
    def maxMoves(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        q = set(range(m))
        
        for j in range(n - 1):
            next_q = set()
            for i in q:
                for next_i in [i - 1, i, i + 1]:
                    if 0 <= next_i < m and grid[next_i][j+1] > grid[i][j]:
                        next_q.add(next_i)
            if not next_q:
                return j
            q = next_q
            
        return n - 1