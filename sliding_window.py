from collections import defaultdict, Counter
from typing import List

"""
i'm a given a list of integers, prices, and each element prices[i] is the price of the stock, neetstock,
at a given date. We need return the maximum profit that I can make. I have to choose a time to buy (i), and 
a time to sell (j) where i < j, I can choose not to buy anything, which would result in 0.

"""
def maximum_stock_price(prices: List[int]) -> int:
  
  """
  will the prices list ever be empty?
  will the array ever have only have value? in which case, should we just return the single value?
  will the element in the array always be valid?
  will the element in the array always be zero and positive?
  since the index is tied to the date, I assume I can't reorder the array?

  Input: prices = [10,1,5,6,7,1]
  Output: 6

  because we buy stock at a price of 1 and sell at 7, we get a profit of 6, which is the highest profit

  
  Input: prices = [10,8,7,5,2]
  Output: 0

  because the price always goes down, we cannot make profit. hence output of 0
  

  brute force / naive solution
  for each element, check every other element to the right (because we cannot sell in the past) to 
  find max profit. Choose the max profit from the saved 


  logic:
  curr_max_profit = 0
  for price in prices
    
    for future_price in prices to the right of price
      if future_price > price and future_price - price > curr_max_profit
        curr_max_profit = future_price - price 
    
  return cuu_max_profit
  """
  curr_max_profit = 0
  for i in range(len(prices)):
    for j in range(i+1, len(prices)):
      if prices[j] > prices[i] and prices[j] - prices[i] > curr_max_profit:
        curr_max_profit = prices[j] - prices[i]
  
  return curr_max_profit



