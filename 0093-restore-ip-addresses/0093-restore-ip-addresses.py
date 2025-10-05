class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = []

        def backtrack(start, path):
            # Base case: 4 segments formed and string is fully used
            if len(path) == 4:
                if start == len(s):
                    res.append(".".join(path))
                return

            # Try segments of length 1 to 3
            for end in range(start, min(start + 3, len(s))):
                part = s[start:end + 1]

                # Rule 1: leading zeros invalid
                if len(part) > 1 and part[0] == '0':
                    break

                # Rule 2: must be <= 255
                if int(part) > 255:
                    break

                backtrack(end + 1, path + [part])

        backtrack(0, [])
        return res

        