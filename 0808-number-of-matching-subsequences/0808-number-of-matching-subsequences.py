from collections import Counter

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        word_freq = Counter(words)
        count = 0
        
        for word, freq in word_freq.items():
            i = 0
            for char in s:
                if i < len(word) and word[i] == char:
                    i += 1
                if i == len(word):  # Word is a subsequence
                    count += freq
                    break
        
        return count
