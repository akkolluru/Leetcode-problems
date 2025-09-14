class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dic = defaultdict(int)
        max_len = 0
        cur = 0
        i = 0
        j = 0
        while j < len(s):

            dic[s[j]] += 1
            cur += 1
            while dic[s[j]] > 1:
                dic[s[i]] -= 1
                i += 1
                cur -= 1
            max_len = max(cur, max_len)
            j += 1

        return max_len