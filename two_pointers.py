from collections import defaultdict, Counter
from typing import List

def validPalindrome(word: str) -> bool:
  leftPointer = 0
  rightPointer = len(word)-1

  while leftPointer < rightPointer:
    if word[leftPointer] == word[rightPointer]:
      leftPointer += 1
      rightPointer += 1
    else:
      if word[leftPointer] != word[rightPointer]:
        return False
      else:
        if not word[leftPointer].isalnum():
          leftPointer += 1
        if not word[rightPointer].isalnum():
          rightPointer -= 1
    return True