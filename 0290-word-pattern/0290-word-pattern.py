class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        
        d={}
        for x in range(len(words)):
            if pattern[x] not in d:
                if words[x] in d.values():
                    return False
                d[pattern[x]] = words[x]
            else:
                if d[pattern[x]]!=words[x]:
                    return False
        return True                    


        