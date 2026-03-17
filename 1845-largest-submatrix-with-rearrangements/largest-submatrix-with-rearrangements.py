class Solution:
    
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])

        # Compute heights of consecutive 1's from top for each cell
        for i in range(1, m):
            for j in range(n):
                if matrix[i][j] == 1:
                    matrix[i][j] += matrix[i-1][j]
        
        max_area = 0
        # For each row, sort heights descending and calculate max rectangle area
        for i in range(m):
            sorted_heights = sorted(matrix[i], reverse=True)
            for j in range(n):
                area = sorted_heights[j] * (j + 1)
                max_area = max(max_area, area)
        
        return max_area