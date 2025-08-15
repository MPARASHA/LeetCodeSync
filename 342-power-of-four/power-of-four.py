class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        """
        100 = 4
        10000 = 16
        """
        if n == 1:
            return True
        if n == 0:
            return False

        try:
            bin_n = [int(i) for i in list(bin(n)[2:])]
        except ValueError:
            return False

        sum_n = sum(bin_n)

        bin_n.reverse()

        index_1 = bin_n.index(1)

        print(bin_n)
        print(index_1)
        
        if sum_n == 1 and index_1 % 2 == 0:
            return True

        else:
            return False

        