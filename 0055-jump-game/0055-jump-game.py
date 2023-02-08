class Solution:
    def canJump(self, nums: List[int]) -> bool:

        curr = nums[0]

        for i in range(1,len(nums)):

            if curr == 0: 
                return False
            curr -= 1

            curr = max(curr, nums[i])
        
        return True
            
