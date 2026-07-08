class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        max_profit = 0
        while r < len(prices):
            # Found a new lowest price (sets buying day)
            # if today is cheaper than my current buy day,
            # every future profit is better using today as the buy point.
            if prices[r] < prices[l]:
                l = r
            # Or we have a higher price, calculate profit
            # and see if it's the highest profit so far
            # and track that.
            else:
                profit = prices[r] - prices[l]
                max_profit = max(profit, max_profit)
            r += 1
        return max_profit
