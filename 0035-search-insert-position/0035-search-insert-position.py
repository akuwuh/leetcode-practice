class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0 
        high = len(nums) - 1 

        while high - low > 1:
            mid = int((high + low)/2)

            if target > nums[mid]: 
                low = mid
            
            if target <= nums[mid]:
                high = mid
            
            

        
        if target <= nums[high] and target > nums[low]:
            return high
        elif target > nums[high]:
            return high + 1
        else: 
            return low