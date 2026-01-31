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


def product_of_array_except_self_division(nums: List[int]) -> List[int]:
  current_product = 1
  products = []

  for num in nums:
    current_product *= num
  
  for num in nums: 
    products.append(int(current_product / num))

  return products

def run():

    print(product_of_array_except_self([1,2,3,4]))
    print(product_of_array_except_self_division([1,2,3,4]))

if __name__ == "__main__":
    run()
