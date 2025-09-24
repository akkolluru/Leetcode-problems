class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        l_sum = sum(cardPoints[:k])
        r_sum = 0
        maxi = l_sum + r_sum
        r = len(cardPoints) - 1
        for i in range(k-1, -1, -1):
            l_sum -= cardPoints[i]
            r_sum += cardPoints[r]
            r -= 1
            maxi = max(maxi, l_sum+r_sum)
        return maxi