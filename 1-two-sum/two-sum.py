class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen = {}
        for i in range(len(nums)):
            left = target-nums[i]
            if left in seen:
                return (seen[left], i)
            else: 
                seen[nums[i]] = i
        