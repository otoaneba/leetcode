"""
LeetCode Hash Table / Dictionary problems
Last updated: 2026-01 by Naoto
"""

from collections import defaultdict, Counter
from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
  return 0

def singleNumber(nums: List[int]) -> int:
  for x in nums:
    count = 0
    for y in nums:
      if y == x:
        count+=1
    if count == 1:
      return x

# [2,2,1]
def singleNumberHashMap(nums: List[int]) -> int:
  seen = set()
  for x in nums:
    if x in seen:
      seen.remove(x)
    else:
      seen.add(x)
  
  return seen.pop()
  
def containsDuplicate(nums: List[int]) -> bool:
  for i, x in enumerate(nums):
    for j, y in enumerate(nums):
      if i == j:
        continue
      if x==y:
        return True
  return False

def containsDuplicateHashMap(nums: List[int]) -> bool:
  seen = set()
  for x in nums:
    if x in seen:
      return True
    else:
      seen.add(x)
      
  return False
        