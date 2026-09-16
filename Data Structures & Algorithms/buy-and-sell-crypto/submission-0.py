class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''
        [10,1,5,6,7,1]  l=0, r=1

        '''

        maxProfit = 0 # base case

        l = 0
        r = 1

        while r < len(prices):
            if prices[l] > prices[r]:
                l=r
                r+=1
                continue
                
            if prices[l] < prices[r]:
                currentProfit = prices[r] - prices[l]
                maxProfit = max(currentProfit, maxProfit)
            
            r+=1
        
        return maxProfit

