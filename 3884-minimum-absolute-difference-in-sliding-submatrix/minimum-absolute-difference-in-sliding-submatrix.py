class Solution:
    def minAbsDiff(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        ans = [[0] * (n - k + 1) for _ in range(m - k + 1)]

        for i in range(m - k + 1):
            for j in range(n - k + 1):
                vals = []

                # Collect all values in the current k x k submatrix
                for x in range(i, i + k):
                    for y in range(j, j + k):
                        vals.append(grid[x][y])

                # Sort and remove duplicates
                vals = sorted(set(vals))

                # If only one unique value, difference is 0
                if len(vals) == 1:
                    ans[i][j] = 0
                    continue

                # Compute minimum absolute difference between distinct elements
                minDiff = float('inf')
                for t in range(1, len(vals)):
                    minDiff = min(minDiff, vals[t] - vals[t - 1])

                ans[i][j] = minDiff

        return ans
        