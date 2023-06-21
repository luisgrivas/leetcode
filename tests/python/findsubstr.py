class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        for word in words:
            tmp = words.copy().remove(word)
            substr = word
            for word2 in tmp:
                if substr not in s:
                    break:
                else:
                    substr += word:
