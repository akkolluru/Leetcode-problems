class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = float('inf')
        min2 = float('inf')

        for i in range(len(nums)):
            if nums[i] > min2:
                return True
            else:
                if nums[i] < min1:
                    min1 = nums[i]
                elif nums[i] < min2 and nums[i] > min1:
                    min2 = nums[i]
        return False
