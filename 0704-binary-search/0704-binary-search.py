class Solution:
    def search(self, nums: List[int], target: int) -> int:
        low = 0 #0 
        high = len(nums) - 1 #5

        while high - low > 1:
            mid = int((high + low)/2)

            if target > nums[mid]: 
                low = mid
            
            if target <= nums[mid]:
                high = mid
            
            

        
        if target == nums[high]:
            return high
        elif target == nums[low]:
            return low
        else:
            return -1
        


        

        
        



