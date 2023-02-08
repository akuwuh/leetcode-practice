class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        ans = len(nums) #min length 
        curr = 0 
        l = 0

        for r,val in enumerate(nums):
            curr += val
            while curr >= target: #if exceed reduce
                ans = min(ans, r-l + 1) #update ans 
                curr -= nums[l]
                l +=1
            
        if l == 0 and target > len(nums):
            return 0

                
        
        return ans
            
                
                
            
                
            
                
                
        
        
        