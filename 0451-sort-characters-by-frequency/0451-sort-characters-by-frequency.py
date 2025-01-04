class Solution:
    def frequencySort(self, s: str) -> str:
        from collections import Counter

        freq = Counter(s)
        sorted_freq = freq.most_common()

        result=''.join(char * count for char,count in sorted_freq)
        return result



        