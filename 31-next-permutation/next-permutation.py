class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        flag = 0
        i = 0
        for i in range(len(nums)-1,0,-1):
            if nums[i] > nums[i-1]:
                flag = 1
                break
        mini = i
        for k in range(len(nums)-1, i-1, -1):
            if nums[k] > nums[i-1]:
                mini = k
                break
        if flag == 0:
            nums.reverse()
        else:
            nums[mini], nums[i-1] =nums[i-1], nums[mini]
            j = len(nums)-1
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
                i += 1
