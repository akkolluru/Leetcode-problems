class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        left = defaultdict(int)
        answer = 0
        for i in range(len(nums)):
            temp = k - nums[i]
            if left[temp] > 0:
                answer += 1
                left[temp] -= 1
            else:
                left[nums[i]] += 1

        return answer

