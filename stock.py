class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        sell = -1
        prof = [0]
        for i in range(1, len(prices)):
            if prices[i] < buy:
                buy = prices[i]
                if sell != -1:
                    prof.append(sell-buy)
                    sell = -1
            elif prices[i] > sell:
                sell = prices[i]
                prof.append(sell-buy)
                sell = -1
        return max(prof)
