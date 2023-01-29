class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:

        if len(nums) == 0: #empty case 
            return [-1,-1] 

        l = 0
        r = len(nums) - 1

        while l < r: #checks for st position (last case possible) while not next to each other, also skips when len == 1 because l = r = 1
            if nums[l] != target:
                l+=1
            if nums[r] != target: #if not found, continue
                r-=1
            if nums[l] == target and nums[r] == target:
                break

        if nums[l] != target and nums[r] != target: #next to each other and did not find or for len == 1 case 
            return [-1,-1]
        
        return [l,r]
    

        #len(nums) = 6
        #0 1 2 3 4 5
        #5 7 7 8 8 10 
        #l         r (l = false) (r = false)
        #  l     r   (l = false) (r = true)
        #    l   r   (l = false) (r = true)
        #      l r   (l = true)  (r = true) -> return [l,r]

        #cases:

        #empty -> return [-1,-1]
        #length 1 w/ out target -> return [-1,-1]
        #length > 1 w/o target -> return [-1,-1]
        #similarities: doesn't have target

        #length 1 w/ target -> return [i,i]
        #length > 1 w/ target == 1 -> return [i,i]

        #length > 1 w/ target > 1 -> return [l,r]



        