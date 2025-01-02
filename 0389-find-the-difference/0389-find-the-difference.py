class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sum=0
        for i in t:
            sum = sum + ord(i)
        for i in s:
            sum = sum - ord(i)
        return chr(sum)

        