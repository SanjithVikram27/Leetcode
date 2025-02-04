class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n<=0:
            return False
        while n%2==0:
            n=n//2
        return n==1

#n/2 is a floating point division
#n//2 is a Integer division