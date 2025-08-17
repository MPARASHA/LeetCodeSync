class Solution:
    def new21Game(self, n: int, k: int, maxPts: int) -> float:
        if k > n:
            return 0.0

        elif k == 0 or k + maxPts <= n:
            return 1.0

        solMat = {}
        solution = 0
        for i in range(k, k + maxPts + 1):
            solution += 1 if i <= n else 0

        for i in range(k-1, -1, -1):
            solMat[i] = solution / maxPts
            remove = 0
            if i + maxPts <= n:
                remove = solMat.get(i + maxPts, 1)

            solution += solMat[i] - remove

        return solMat[0]
            