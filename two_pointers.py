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

  
def moveZerosToEnd(arr: List[int]) -> List[int]:
    observer = 0
    bookkeeper = 0
    while observer < len(arr):
        if arr[observer] != 0:
            temp = arr[observer]
            arr[observer] = arr[bookkeeper]
            arr[bookkeeper] = temp
            bookkeeper += 1

        observer += 1
    return arr

def moveZerosToEndAlt(arr: List[int]) -> List[int]:
    bookkeeper = 0
    for num in arr:
        if num != 0:
            arr[bookkeeper] = num 
            bookkeeper += 1

    for remaining_index in range(bookkeeper, len(arr)):
      arr[remaining_index] = 0

    return arr

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeLinkedLists(list1: ListNode, list2: ListNode) -> ListNode:
  if list1 == None:
    return list2
  elif list2 == None:
    return list1
  
  dummy = ListNode(0)
  tail = dummy
  while list1 != None and list2 != None:
    if list1.val <= list2.val:
      tail.next = list1
      tail = tail.next
      list1 = list1.next
    else:
      tail.next = list2
      tail = tail.next
      list2 = list2.next
  if list1 != None:
      tail.next = list1
  elif list2 != None:
      tail.next = list2
  return dummy.next

def prefixSum(arr: List[int], k: int) -> int:
  prefix_count = {0: 1}
  count = 0
  current_sum = 0

  for num in arr:
    current_sum += num
    if current_sum - k in prefix_count:
      count += prefix_count[current_sum - k]
    prefix_count[current_sum - k] = prefix_count.get(current_sum - k, 0) + 1
  return count

# Finding the length of a cycle in a linked list
def length_of_cycle(head: ListNode) -> int:

  if head and head.next == None:
    return 0

  slow = fast = head
  while fast and fast.next:
    slow = slow.next
    fast = fast.next.next
    if slow == fast:
      count = 1
      slow = slow.next
      while slow != fast:
        slow = slow.next
        count += 1
        if slow == fast:
          return count
  return 0