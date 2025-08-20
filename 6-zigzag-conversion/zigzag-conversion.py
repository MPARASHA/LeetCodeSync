class Solution:
    def convert(self, s: str, numRows: int) -> str:
        matrix = [[] for _ in range(numRows)]


        while len(s) > 0:
            for i in range(numRows):
                if len(s) == 0:
                    break
                matrix[i].append(s[0])
                s = s[1:]

            for j in range(numRows-2, 0, -1):
                if len(s) == 0:
                    break
                matrix[j].append(s[0])
                s = s[1:]

        output = ""

        #print(matrix)

        for row in matrix:
            output += "".join(row)

        return output


