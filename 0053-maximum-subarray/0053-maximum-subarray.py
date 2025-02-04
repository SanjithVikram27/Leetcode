class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        sum=0

        for i in range(len(nums)):
            if sum<0:
                sum=0
                
            sum = sum + nums[i]
            max_sum=max(sum,max_sum)

        return max_sum

        