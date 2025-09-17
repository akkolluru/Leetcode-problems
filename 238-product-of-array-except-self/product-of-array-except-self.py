class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        forward = [1]
        back = [1]*len(nums)


        #forward pass:
        for i in range(1, len(nums)):
            forward.append(nums[i-1]*forward[i-1])
        #backward pass:
        for j in range(len(nums)-2, -1, -1):
            back[j] = nums[j+1] * back[j+1]
        print(forward, back)
        answer = []
        for k in range(len(nums)):
            answer.append(forward[k]*back[k])
        
        return answer
