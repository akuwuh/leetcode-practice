class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) -1

        if len(nums) == 1 or nums[l] < nums[r]: # length of 1 or in original position
            return nums[0]

        # means not in original position

        while r - l > 1:
            m = (l+r)//2

            if nums[r] < nums[m]: 
                l = m
            if nums[l] > nums[m]:
                r = m
            
        return min(nums[l], nums[r])

    # general algorithm, whichever of nums[l] or  nums[r]is greater becomes m until next to each other. return min of both

    # 0 1 2 3 4 
    # 3 4 5 1 2
    # l   m   r  l > r -> l = m
    #     l m r  l > r -> l = m 
    #       l r  

    # 0 1 2 3 4 5 6 
    # 4 5 6 7 0 1 2
    # l     m     r
    #       l m   r
    #       l r
    # return whichever one is bigger min(l,r)


    # 0  1  2  3
    # 11 13 15 17
    # l  m     r l < r -> r = m
    # l  r       
    #return min(l,r)

    #  0  1  2  3  4
    # -4 -5 -1 -2 -3 
    #  l     m     r
    #  l  m  r
    #      

    # 0 1 2  3  4 5
    # 1 2 3 -2 -1 0
    # l   m       r
    #     l  m    r
    #        l  m r
    #        l  r

    # 0 1 2 3 4
    # 5 1 2 3 4
    # l   m   r



