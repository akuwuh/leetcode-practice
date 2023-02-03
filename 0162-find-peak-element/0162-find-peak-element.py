class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
    
        if len(nums) == 1:
            return 0

        l, r = 0, len(nums) -1

        while l < r:

            m = (l + r)//2

            if nums[m-1] < nums[m]and nums[m] > nums[m + 1]: # if m is peak, return m
                return m
            elif nums[m+1] > nums[m]: #peak occurs on the right
                l = m + 1
            else:
                r = m - 1
        return l
    
    # 1 2
    # l r
    # m 
    # 
            
    
    # 1 2 3 1 
    # l m   r -> nums[l] = 1, nums[m] = 2, nums[r] = 1
    #   l m r
    
    # 0 1 2 3 4 5 6 
    # 1 2 1 3 5 6 4
    # l     m     r
    #       l m   r
    #         l m r
    
    # we have to get to the configuration where l,m, and r are next each other and m is the largest of the two 