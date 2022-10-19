class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_val = 0; #max value of the ones seen before
        max_difference = 0; 
        for i in range(len(prices)-1, -1, -1):
            if prices[i] > max_val:
                max_val = prices[i]
            
            curr_difference = max_val - prices[i]
            
            if curr_difference > max_difference:
                max_difference = curr_difference
        
        return max_difference
                       
        
                       
            