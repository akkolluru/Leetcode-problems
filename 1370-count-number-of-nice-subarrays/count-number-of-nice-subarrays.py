class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        def atMost(K):
            l = 0
            odds = 0
            res = 0
            for r, x in enumerate(nums):
                if x % 2: odds += 1
                while odds > K:
                    if nums[l] % 2: odds -= 1
                    l += 1
                res += r - l + 1
            return res
        return atMost(k) - atMost(k - 1)