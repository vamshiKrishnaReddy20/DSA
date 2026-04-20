class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
       
        for i in range(k // 2):  # Flip the k x k submatrix vertically
            for j in range(y, y + k): # Swap row x + i with row x + k - 1 - i
                grid[x + i][j], grid[x + k - 1 - i][j] = grid[x + k - 1 - i][j], grid[x + i][j]
        return grid