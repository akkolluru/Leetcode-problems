class Solution:
    def frequencySort(self, s: str) -> str:
        dic = Counter(s)
        items = list(dic.items())
        items.sort(key = lambda x: x[1])
        answer = ""
        print(items)
        for st, num in items[::-1]:
            answer += st*num
        return answer