class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        ind = 0

        for ch in t:
            if ind == len(s):
                return True
            if s[ind] == ch:
                ind += 1
        return ind == len(s)