class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        #
        def calc_days(weights, cap): # function that simulates how many days it takes to ship out all packages given maximum capacity
            days = 0
            curr = 0
            for i in weights:
                if curr + i > cap:
                    curr = 0
                    days +=1

                curr+=i

            return days + 1
 
        if days == 1 or len(weights) == 1: # edge + corner case for 1
            return sum(weights)

        l, r = max(weights) , sum(weights) # assigns to minimum and maximum weight ship should be able to carry
                                           # considering cases of days = len(weights) and days = 1
        while l<r: # binary search
            m = (l + r)//2 # weight to be checked
            m_days = calc_days(weights, m)

            if m_days == days:
                m-=1
                while calc_days(weights, m) == days:
                    m-=1
                return m+1
            
            elif m_days > days:
                l = m + 1
            
            else: # m_days < days
                r = m 
        return l