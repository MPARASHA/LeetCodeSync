class Solution:
    def findMedianSortedArrays(self, n: List[int], m: List[int]) -> float:
        
        i = 0
        for elem in n:
            if len(m) == 0 or elem <= m[0]:
                m.insert(0, elem)
                continue
            elif elem >= m[-1]:
                m.insert(len(m), elem)
                continue
            for j in range(i, len(m)-1):
                if m[j] <= elem <=m[j+1]:
                    m.insert(j+1, elem)
                    i = j+1
                    break
                

        size = len(m)

        if size%2 != 0:
            print(m)
            return m[size//2]
        else:
            print(m)
            return (m[(size//2) - 1] + m[(size//2)])/2










        