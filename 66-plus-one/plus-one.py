class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        add = 1
        for i in range(len(digits)-1, -1, -1):
            summ = carry + add + digits[i]
            carry = summ // 10
            add = 0

            digits[i] = summ%10
        if carry != 0:
            return [1] + digits
        else:
            return digits


