# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        
        high = n  
        low = 1
        
        if (isBadVersion(1)):
            return 1
        
        while high - low > 1:
            mid = int((high + low)/2)
            if (isBadVersion(mid)):
                high = mid
            else:
                low = mid
            
        
        if (isBadVersion(high)):
            return high
        else:
            return low