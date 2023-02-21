class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 1: return nums[0]
        l, r = 0, n - 1
        # cases:

        # if m and m - 1 is the same val and r - m is even -> on left
        # else if r - m is odd -> on right

        # m and m + 1 is the same val and m - l is even -> on right
        # else if m - l is odd -> on left 
        
        # on right assign l = m + 1
        # on left assign r = m - 1

        # 0 1 2  3  4  5  6 
        #[7,7,10,11,11,12,12]

        while r - l > 1:
            m = (l+r)//2
            if nums[m-1] != nums[m] and nums[m+1] != nums[m]: #case where m is single val   
                return nums[m]

            elif nums[m] == nums[m-1]:
                if (r-m)%2 == 0: r = m
                else: l = m + 1

            else: # nums[m] == nums[m+1]
                if (m-l)%2 == 1: r = m - 1
                else: l = m
        return nums[l] if nums[m] == nums[m+1] else nums[r]

            