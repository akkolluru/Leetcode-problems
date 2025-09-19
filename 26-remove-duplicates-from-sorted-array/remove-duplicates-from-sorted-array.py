class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1
        while i < len(nums):
            print(i, len(nums))
            if i > 0:
                if nums[i] == nums[i-1]:
                    nums.pop(i-1)
                    i -= 1
                else:
                    i += 1
            else:
                i += 1
        return len(nums)