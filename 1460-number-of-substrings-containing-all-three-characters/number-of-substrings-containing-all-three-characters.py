class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        seen = {'a': -1, 'b' : -1, 'c' : -1}
        count = 0

        for i, x in enumerate(s):
            print(seen)
            seen[x] = i
            if seen['a'] != -1 and seen['b'] != -1 and seen['c'] != -1:
                count += 1 + min(seen['a'], seen['b'], seen['c'])
        
        return count