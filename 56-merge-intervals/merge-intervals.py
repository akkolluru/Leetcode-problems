class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []
        
        intervals.sort(key=lambda x: x[0])
        merged = [intervals[0]]

        for i in range(len(intervals)):
            curr = intervals[i]
            last_interval = merged[-1]

            if curr[0] <= last_interval[1]:
                last_interval[1] = max(last_interval[1], curr[1])
            else:
                merged.append(curr)
        return merged
        
        