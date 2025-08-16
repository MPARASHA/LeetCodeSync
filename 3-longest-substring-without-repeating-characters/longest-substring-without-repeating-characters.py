class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxLen = 0
        sub = ""
        currLen = 0
        for c in s:
            print(c + sub)
            if c in sub:
                sub+= c
                sub = sub.split(c,1)[1]
                currLen = len(sub)
            else:
                sub+= c
                currLen += 1
                if currLen > maxLen:
                    maxLen = currLen

        return maxLen

        