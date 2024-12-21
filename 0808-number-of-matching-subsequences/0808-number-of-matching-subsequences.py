from collections import Counter

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        word_freq = Counter(words)  # Count each word's frequency
        count = 0
        
        for word, freq in word_freq.items():  # Iterate over unique words and their counts
            i = 0
            for char in s:
                if i < len(word) and word[i] == char:
                    i += 1
                if i == len(word):  # If the word is a subsequence
                    count += freq  # Add its frequency to the count
                    break
        
        return count
