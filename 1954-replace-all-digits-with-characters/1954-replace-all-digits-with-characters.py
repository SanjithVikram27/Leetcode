class Solution:
    def replaceDigits(self, s: str) -> str:
        result=[]

        for i in range(len(s)):
            if i%2==0:
                result.append(s[i])
            else:
                shifted_char = chr(ord(s[i-1]) + int(s[i]))
                result.append(shifted_char)

        return ''.join(result)





        