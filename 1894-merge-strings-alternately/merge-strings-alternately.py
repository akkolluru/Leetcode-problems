class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        answer = []
        count = 0
        for i in range(min(len(word1), len(word2))):
            answer.append(word1[i])
            answer.append(word2[i])
            count += 1
        
        while count < len(word1):
            answer.append(word1[count])
            count += 1
        while count < len(word2):
            answer.append(word2[count])
            count += 1
        return "".join(answer)