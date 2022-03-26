class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        prices.insert(0, 99999)
        prices.append(-1)
        buy = -1
        prof = 0
        for i in range(1, len(prices)-1):
            # buy at local minima
            if prices[i] <= prices[i-1] and prices[i] < prices[i+1]:
                buy = prices[i]
            # sell at local maxima
            elif buy >= 0 and prices[i] > prices[i-1] and prices[i] >= prices[i+1]:
                prof += prices[i]-buy
                buy = -1
        return prof  
