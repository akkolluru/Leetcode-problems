class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        answer = []
        balance = 0
        for i in s:
            if i == "(" and balance > 0:
                answer.append(i)
            if i == ")" and balance > 1:
                answer.append(i)
            balance += 1 if i == "(" else -1

        return "".join(answer)

