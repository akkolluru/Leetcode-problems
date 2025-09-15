from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""

        need = Counter(t)
        missing = len(t)
        left = 0
        best_len = float('inf')
        best_l = 0

        for right, ch in enumerate(s):
            if ch in need:
                need[ch] -= 1
                if need[ch] >= 0:         
                    missing -= 1

            # window valid: try to shrink
            while missing == 0:
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_l = left

                left_ch = s[left]
                if left_ch in need:
                    need[left_ch] += 1
                    if need[left_ch] > 0:  
                        missing += 1
                left += 1

        return "" if best_len == float('inf') else s[best_l: best_l + best_len]