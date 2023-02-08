class Solution:
    def jump(self, nums: List[int]) -> int:
        nums.pop()
        n = len(nums)
        if n <= 1:
            return n
        
        if nums[0] > n-1:
            return 1
        
        if nums[0] == n-1:
            return 2

        counter = 1
        curr = nums[0] 
        globalreach = 0 


        for i,j in enumerate(nums):
            val = j + i
            if val >= n:
                counter +=1
                break

            if i < curr: 
                globalreach = max(globalreach,val)
                continue
            counter+=1
            curr = max(globalreach,val)
            
        return counter
  



            
            