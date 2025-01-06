class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result= ""

        while columnNumber>0:
            columnNumber-=1
            char = chr(columnNumber%26 + ord('A'))
            result = char + result
            columnNumber = columnNumber//26
        return result
        