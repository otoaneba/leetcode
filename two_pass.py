from collections import defaultdict, Counter
from typing import List

def product_of_array_except_self(nums: List[int]) -> List[int]:
 
  # first pass left to right
  current_product = 1
  products= []
  
  for num in nums:
    products.append(current_product)
    current_product *= num
  
  # second pass right to left
  current_product = 1
  for i in reversed(range(len(nums))):
    products[i] *= current_product
    current_product *= nums[i]
  
  return products
  # [1, 2, 3, 4] output: [24, 12, 8, 6]
  #  
  #  1  2  6  24
  # [1, 1, 2, 6]
  #           
  # [   12  8  6]
  #         8  4

  # [2, 3, 4, 5] output: [60, 40, 30, 24]
  # [0, 2, 6, 24]
  # [60  20  5  0]

def run():

    print(product_of_array_except_self([1,2,3,4]))

if __name__ == "__main__":
    run()
