class Solution:
    def longestPalindrome(self, s: str) -> str:
        output = s[0]
        pallindromes = {}
        for i in range(1, len(s)):
            for j in range(len(s)):
              
                if j+i+1 <= len(s) and s[j] == s[j+i] and (i <= 2 or pallindromes.get((j+1, j+i-1), False)):
                    pallindromes[(j, j+i)] = True
                    if len(s[j:j+i+1]) > len(output):
                        output = s[j:j+i+1]
                        


        return output
