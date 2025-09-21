class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if not stack:
                stack.append(i)
            else:
                if i in "({[":
                    stack.append(i)
                elif i == ")" and stack[-1] == "(":
                    stack.pop()
                elif i == "]" and stack[-1] == "[":
                    stack.pop()
                elif i == "}" and stack[-1] == "{":
                    stack.pop()          
                else:
                    return(False)
        return len(stack) == 0      

        