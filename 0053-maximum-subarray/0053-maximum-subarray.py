class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxs = nums[0]
        curr = 0
        
        for i in nums:
            if curr<0:
                curr = 0
            
            curr += i 
            maxs = max(maxs, curr)
        
        return maxs