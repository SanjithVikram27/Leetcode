class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()  # Step 1: Sort to handle duplicates
        
        def backtrack(start, path):
            res.append(path[:])  # Add current subset
            for i in range(start, len(nums)):
                # Step 2: Skip duplicates at same recursion level
                if i > start and nums[i] == nums[i - 1]:
                    continue
                backtrack(i + 1, path + [nums[i]])
        
        backtrack(0, [])
        return res

        