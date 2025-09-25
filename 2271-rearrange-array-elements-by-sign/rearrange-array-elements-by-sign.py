class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = []
        neg = []
        answer = []
        for i in nums:
            if i < 0:
                neg.append(i)
            else:
                pos.append(i)
        

        for i in range(len(pos)):
            answer.append(pos[i])
            answer.append(neg[i])

        return answer