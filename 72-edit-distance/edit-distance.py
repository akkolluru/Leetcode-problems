class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        l1 = len(word1) + 1
        l2 = len(word2) + 1

        dp = [[0 for _ in range(l1)] for _ in range(l2)]

        for i in range(l1):
            dp[0][i] = i
        for j in range(l2):
            dp[j][0] = j
    
        for r in range(1, l2):
            for c in range(1, l1):
                if word2[r-1] == word1[c-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:
                    dp[r][c] = 1 + min(
                        dp[r-1][c-1],
                        dp[r-1][c],
                        dp[r][c-1]
                    )
        return dp[l2-1][l1-1]