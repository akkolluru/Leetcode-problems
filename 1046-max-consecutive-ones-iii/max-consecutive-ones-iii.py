class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        max_len = 0
        length = 0
        l = 0
        for r in range(len(nums)):
            if nums[r] == 1:
                length += 1
            else:
                k -= 1
                length += 1
            
            while k < 0:
                if nums[l] == 0:
                    k += 1
                l += 1
                length -= 1
            max_len = max(max_len, length)
        return max_len

