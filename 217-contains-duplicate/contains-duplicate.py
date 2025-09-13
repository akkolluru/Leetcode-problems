class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_map = collections.defaultdict(int)
        for i in nums:
            num_map[i] += 1
            if num_map[i] > 1:
                return True
        return False