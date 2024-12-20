from collections import defaultdict
from typing import List

class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        # Group words by their first character
        waiting = defaultdict(list)
        for word in words:
            waiting[word[0]].append(iter(word[1:]))  # Store iterator for the rest of the word

        count = 0
        # Process each character in string s
        for char in s:
            # Get words waiting for this character
            current_words = waiting[char]
            waiting[char] = []  # Clear the list for this character
            
            for it in current_words:
                nxt = next(it, None)  # Move iterator to the next character
                if nxt:  # If there are more characters to match
                    waiting[nxt].append(it)
                else:  # If the word is completely matched
                    count += 1

        return count

        