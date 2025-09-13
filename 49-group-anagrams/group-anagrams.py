class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        word_dic = collections.defaultdict(list)

        for s in strs:
            st = "".join(sorted(s))
            word_dic[st].append(s)
        return list(word_dic.values())
        