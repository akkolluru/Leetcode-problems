class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        digit = {
    "2":"abc","3":"def","4":"ghi","5":"jkl",
    "6":"mno","7":"pqrs","8":"tuv","9":"wxyz"
    }
        if digit == "":
            return []
        
        def backtrack(path, index):
            if index == len(digits):
                answer.append("".join(path))
                return

            for ch in digit[digits[index]]:
                path.append(ch)
                backtrack(path, index+1)
                path.pop()
        answer = []
        backtrack([], 0)
        return answer
        
