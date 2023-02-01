class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 4,5,6,7,0,1,2

        #find pivot index if not in ascending order
        #first and last element will always be larger if pivoted
        # check l r to see if pivoted 

        def search(nums: List[int], target: int): #function for searching for index (in ascending order) using binary search
            if len(nums) == 1 and nums[0] == target: #if 1 and has return
                return 0

            l,r= 0, len(nums) -1
            while l<=r: #loop till they are next to each other works for  > 1
                m = (r + l)//2
                
                if nums[m] == target:
                    return m
                elif nums[m] < target:
                    l = m+1
                else:
                    r = m-1
            return -1

        if (nums[0] <= nums[len(nums)-1]): #not pivoted
            return search(nums, target)
        else: #pivoted, we search for part where it is pivoted and divide into subarrays
            l,r = 0, len(nums) - 1

            while r - l != 1: #while not togther   
                m  = (r + l)// 2

                if nums[l] > nums[m]: #pivot is on left side
                    r = m 
                
                if nums[r] < nums[m]: #pivot is on right side
                    l = m
            

            p = r
            one = search(nums[:p], target)
            two = search(nums[p:], target)

            if one == two == -1:
                return -1

            if one != -1:
                return one
            if two != -1:
                return two + p
        #testcase:
        # 4 5 6 7 0 1 2
        # l     m     r since l < m -> not pivot on right side -> have l = m
        #       l m   r since l > m -> pivot is on the left side -> r = m 
        #       l r     since next to each other(r - l = 1), one of them is pivot

        # after binary search 0 - p then p - end [:p] [p:]





        # if in ascending order find index through simple binary search

        #len = 7
        #l = 0
        #r = 6
        # 1 2 3 4 5 6 7
        # l     m   t r
        #         l t r


                

            
            







