class Solution:
    def reverse(self, x: int) -> int:
        st = str(abs(x))
        if int(st[::-1]) > 2147483647:
            return 0
        if x<0:
            return -int(st[::-1])
        else:
            return int(st[::-1])
