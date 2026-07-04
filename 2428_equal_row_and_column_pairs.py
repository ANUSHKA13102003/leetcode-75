from collections import Counter

class Solution:
    def equalPairs(self, grid):
        row_count = Counter(tuple(row) for row in grid)

        count = 0
        n = len(grid)

        for col in range(n):
            column = tuple(grid[row][col] for row in range(n))
            count += row_count[column]

        return count