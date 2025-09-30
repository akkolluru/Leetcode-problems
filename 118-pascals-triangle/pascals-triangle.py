class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        answer = [[1]]
        n = numRows
        for i in range(2, n + 1):
            temp = [1]
            for j in range(1, i - 1):
                temp.append(answer[-1][j-1] + answer[-1][j])
            temp.append(1)
            answer.append(temp)
        
        return answer
        