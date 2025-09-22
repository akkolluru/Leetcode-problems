class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []

        def backtrack(index, remaining, path):
            if remaining == 0:
                answer.append(path.copy())
                return
            if remaining < 0 or index == len(candidates):
                return
            
            path.append(candidates[index])
            backtrack(index, remaining - candidates[index], path)

            path.pop()
            backtrack(index + 1, remaining, path)
        backtrack(0, target, [])
        return answer