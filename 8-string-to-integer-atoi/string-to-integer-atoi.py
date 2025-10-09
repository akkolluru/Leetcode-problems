class Solution:
    def myAtoi(self, s: str) -> int:
        answer = 0
        sign = 1
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        s = s.strip()
        for i in range(len(s)):
            if i == 0 and s[i] == "-":
                sign = -1
            elif i == 0 and s[i] == "+":
                sign = 1
            else:
                if s[i] in "0123456789":
                    answer = answer * 10 + int(s[i])
                else:
                    break
        if answer*sign > INT_MAX:
            return INT_MAX
        elif answer*sign < INT_MIN:
            return INT_MIN
        else:
            return answer*sign
