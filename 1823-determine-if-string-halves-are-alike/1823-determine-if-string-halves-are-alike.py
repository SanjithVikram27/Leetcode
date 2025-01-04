class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = {'a','e','i','o','u','A','E','I','O','U'}

        mid=len(s)//2
        a,b = s[:mid],s[mid:]

        count_a = sum(1 for char in a if char in vowels)
        count_b = sum(1 for char in b if char in vowels)

        return count_a == count_b       