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


def palindromNumberStringConversion(num: int) -> bool:
  if num < 0:
    return False
  elif num % 10 == 0 and num > 0:
    return False 

  stringifiedNum = str(num)

  leftPointer = 0
  rightPointer = len(stringifiedNum)-1

  while leftPointer < rightPointer:
    if stringifiedNum[leftPointer] == stringifiedNum[rightPointer]:
      leftPointer += 1
      rightPointer += 1
    else:
      if stringifiedNum[leftPointer] != stringifiedNum[rightPointer]:
        return False
      else:
        if not stringifiedNum[leftPointer].isalnum():
          leftPointer += 1
        if not stringifiedNum[rightPointer].isalnum():
          rightPointer -= 1
    return True

def palindromeNumber(num: int) -> bool:
  if num < 0:
    return False
  elif num % 10 == 0 and num > 0:
    return False 

  reversed_digits = 0
  count = 0
  while reversed_digits < num:
    last_digit = num % 10 # get the last digit
    reversed_digits = (reversed_digits * 10) + last_digit # add the last digit to reversed_digit
    num = num // 10  # take the last digit out of num
    count += 1 # count how many digits we iterate through 
  
  if reversed_digits > num:
    return (reversed_digits // 10) == num
  else:
    return reversed_digits == num

  

  

