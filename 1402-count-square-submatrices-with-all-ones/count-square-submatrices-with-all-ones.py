class Solution:
    def countSquares(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        count = 0
        sizeMax = min(m,n)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                for k in range(sizeMax):
                    if i + k < m and j + k < n and matrix[i][j] == 1 and matrix[i+k][j+k]== 1:
                        if k == 0:
                            count += 1
                        else:
                            zeroFound = False
                            for l in range(i, i+k):
                                if matrix[l][j+k] == 0:
                                    zeroFound = True
                                    break

                            if zeroFound:
                                break
                            for p in range(j, j+k):
                                if matrix[i+k][p] == 0:
                                    zeroFound = True
                                    break

                            if zeroFound:
                                break

                            count += 1
                    else:
                        break

        return count
                        
        