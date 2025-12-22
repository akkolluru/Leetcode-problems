class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = {}
        for num in nums:
            if num in num_map:
                num_map[num] += 1
            else:
                num_map[num] = 1
        heap = []
        answer = []
        for key, val in num_map.items():
            heapq.heappush(heap, (-val, key))
        for i in range(k):
            answer.append(heapq.heappop(heap)[1])

        return answer