def maxProfit(prices):
    lowest = prices[0]
    max_profit = 0
    for i in prices:
        if i < lowest:
            lowest = i
        max_profit = max(max_profit, i - lowest)
    return max_profit
print(maxProfit([7,1,5,3,6,4]))