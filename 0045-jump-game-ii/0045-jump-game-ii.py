class Solution:
    def jump(self, nums: List[int]) -> int:
        
        def maxreach(sub: List[int]): #returns index that has the most reach
            if len(sub) == 1:
                return 0
            maxi = 0
            index = 0
            for i,val in enumerate(sub):
                if i + val >= maxi:
                    maxi = i + val
                    index = i
            return index
        
        if len(nums) == 1:
            return 0
        
        if len(nums) == 2:
            return 1

        if nums[0] == len(nums) - 2:
            return 2

        i = 0
        counter = 0
        
        while nums[i] + i < len(nums)- 1:

            if nums[i] >= len(nums) - 1:
                break
            
            lol = nums[i+1: i+ nums[i] + 1]
            i += maxreach(lol) + 1
            counter +=1

            print(i)
        
        return counter + 1
            
            
            