class Solution:
    def grayCode(self, n: int) -> List[int]:
        res = []
        for i in range(1 << n):  # 1 << n = 2^n
            res.append(i ^ (i >> 1))  # Gray code formula
        return res

        