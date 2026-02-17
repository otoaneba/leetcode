from collections import defaultdict, Counter
import heapq
from typing import List


# You are given an integer array nums of length n. Create an array ans of length 2n where ans[i] == nums[i] and ans[i + n] == nums[i] for 0 <= i < n (0-indexed).

# Specifically, ans is the concatenation of two nums arrays.

# Return the array ans.

# Example 1:

# Input: nums = [1,4,1,2]

# Output: [1,4,1,2,1,4,1,2]
# Example 2:

# Input: nums = [22,21,20,1]

# Output: [22,21,20,1,22,21,20,1]
# Constraints:

# 1 <= nums.length <= 1000.
# 1 <= nums[i] <= 1000
def getConcatenation(self, nums: List[int]) -> List[int]:
        ans = []
        for num in nums:
            ans.append(num)
        for num in nums:
            ans.append(num)
        return ans


# Given an integer array nums, return true if any value appears more than once in the array, otherwise return false.

# Example 1:

# Input: nums = [1, 2, 3, 3]

# Output: true

# Example 2:

# Input: nums = [1, 2, 3, 4]

# Output: false

def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num not in seen:
                seen.add(num)
            else:
                return True
        return False

# Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: s = "racecar", t = "carrace"

# Output: true
# Example 2:

# Input: s = "jar", t = "jam"

# Output: false
def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        set1 = {}
        set2 = {}
        for i in range(len(s)):
            if s[i] not in set1:
                set1[s[i]] = 1
            else:
                set1[s[i]] += 1
            if t[i] not in set2:
                set2[t[i]] = 1
            else:
                set2[t[i]] += 1
        return set1 == set2

# Longest Common Prefix
# Solved 
# Easy
# Topics
# Company Tags
# You are given an array of strings strs. Return the longest common prefix of all the strings.

# If there is no longest common prefix, return an empty string "".

# Example 1:

# Input: strs = ["bat","bag","bank","band"]

# Output: "ba"
# Example 2:

# Input: strs = ["dance","dag","danger","damage"]

# Output: "da"
# Example 3:

# Input: strs = ["neet","feet"]

# Output: ""
# Constraints:

# 1 <= strs.length <= 200
# 0 <= strs[i].length <= 200
# strs[i] is made up of lowercase English letters if it is non-empty.

def longestCommonPrefix(self, strs: List[str]) -> str:
        # edge cases:
        # empty array
        # array with only one value
        if len(strs) == 0:
            return ""
        if len(strs) == 1:
            return strs[0]

        # set prefix as first value, then iterate starting from the second element
        currLongestPrefix = strs[0]
        for i in range(1, len(strs)):
            for j in range(len(currLongestPrefix)):
                if j > len(strs[i])-1:
                    currLongestPrefix = currLongestPrefix[:len(strs[i])]
                    break
                if currLongestPrefix[j] != strs[i][j]:
                    currLongestPrefix = currLongestPrefix[:j]
                    break
        return currLongestPrefix

# Remove Element
# Solved 
# Easy
# Topics
# Company Tags
# You are given an integer array nums and an integer val. Your task is to remove all occurrences of val from nums in-place.

# After removing all occurrences of val, return the number of remaining elements, say k, such that the first k elements of nums do not contain val.

# Note:

# The order of the elements which are not equal to val does not matter.
# It is not necessary to consider elements beyond the first k positions of the array.
# To be accepted, the first k elements of nums must contain only elements not equal to val.
# Return k as the final result.

# Example 1:

# Input: nums = [1,1,2,3,4], val = 1

# Output: [2,3,4]
# Explanation: You should return k = 3 as we have 3 elements which are not equal to val = 1.

# Example 2:

# Input: nums = [0,1,2,2,3,0,4,2], val = 2

# Output: [0,1,3,0,4]
# Explanation: You should return k = 5 as we have 5 elements which are not equal to val = 2.

# Constraints:

# 0 <= nums.length <= 100
# 0 <= nums[i] <= 50
def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        writeIndex = 0

        for observerIndex, currValue in enumerate(nums):
            if currValue != val:
                nums[writeIndex] = currValue
                count += 1
                writeIndex += 1
        return count


# Design a HashSet without using any built-in hash table libraries.

# Implement MyHashSet class:

# void add(key) Inserts the value key into the HashSet.
# bool contains(key) Returns whether the value key exists in the HashSet or not.
# void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
# Example 1:

# Input: ["MyHashSet", "add", "add", "contains", "contains", "add", "contains", "remove", "contains"]
# [[], [1], [2], [1], [3], [2], [2], [2], [2]]

# Output: [null, null, null, true, false, null, true, null, false]
# Explanation:
# MyHashSet myHashSet = new MyHashSet();
# myHashSet.add(1); // set = [1]
# myHashSet.add(2); // set = [1, 2]
# myHashSet.contains(1); // return True
# myHashSet.contains(3); // return False, (not found)
# myHashSet.add(2); // set = [1, 2]
# myHashSet.contains(2); // return True
# myHashSet.remove(2); // set = [1]
# myHashSet.contains(2); // return False, (already removed)

# Constraints:

# 0 <= key <= 1,000,000
# At most 10,000 calls will be made to add, remove, and contains.
class MyHashSet:

      # def __init__(self):
    #     self.size = 10_000
    #     self.buckets = [[] for _ in range(self.size)]

    # def add(self, key: int) -> None:
    #     hash_value = key % self.size

    #     if key not in self.buckets[hash_value]:
    #         self.buckets[hash_value].append(key)
        
    # def remove(self, key: int) -> None:
    #     hash_value = key % self.size

    #     if key in self.buckets[hash_value]:
    #         self.buckets[hash_value].remove(key)

    # def contains(self, key: int) -> bool:
    #     hash_value = key % self.size

    #     return key in self.buckets[hash_value]

  def __init__(self):
      self.buckets = [False] * 1_000_001

  def add(self, key: int) -> None:
      self.buckets[key] = True
      
  def remove(self, key: int) -> None:
      self.buckets[key] = False

  def contains(self, key: int) -> bool:
      return self.buckets[key] == True

# Design a HashMap without using any built-in hash table libraries.

# Implement the MyHashMap class:

# MyHashMap() initializes the object with an empty map.
# void put(int key, int value) inserts a (key, value) pair into the HashMap. If the key already exists in the map, update the corresponding value.
# int get(int key) returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
# void remove(key) removes the key and its corresponding value if the map contains the mapping for the key.
# Example 1:

# Input: ["MyHashMap", "put", "put", "get", "get", "put", "get", "remove", "get"]
# [[], [1, 1], [2, 2], [1], [3], [2, 1], [2], [2], [2]]

# Output: [null, null, null, 1, -1, null, 1, null, -1]
# Explanation:
# MyHashMap myHashMap = new MyHashMap();
# myHashMap.put(1, 1); // The map is now [[1,1]]
# myHashMap.put(2, 2); // The map is now [[1,1], [2,2]]
# myHashMap.get(1); // return 1, The map is now [[1,1], [2,2]]
# myHashMap.get(3); // return -1 (i.e., not found), The map is now [[1,1], [2,2]]
# myHashMap.put(2, 1); // The map is now [[1,1], [2,1]] (i.e., update the existing value)
# myHashMap.get(2); // return 1, The map is now [[1,1], [2,1]]
# myHashMap.remove(2); // remove the mapping for 2, The map is now [[1,1]]
# myHashMap.get(2); // return -1 (i.e., not found), The map is now [[1,1]]

# Constraints:

# 0 <= key, value <= 1,000,000
# At most 10,000 calls will be made to put, get, and remove.

class MyHashMap:

    def __init__(self):
        self.buckets = [-1] * 1_000_001

    def put(self, key: int, value: int) -> None:
        self.buckets[key] = value

    def get(self, key: int) -> int:
        return self.buckets[key]

    def remove(self, key: int) -> None:
        self.buckets[key] = -1

    # def __init__(self):
    #     self.size = 10_000
    #     self.buckets = [[] for _ in range(self.size)]

    # def put(self, key: int, value: int) -> None:
    #     hash_value = key % self.size
    #     for pair in self.buckets[hash_value]:
    #         if pair[0] == key:
    #             pair[1] = value
    #             return    
    #     self.buckets[hash_value].append([key, value])
        

    # def get(self, key: int) -> int:
    #     hash_value = key % self.size
    #     for pair in self.buckets[hash_value]:
    #         if pair[0] == key:
    #             return pair[1]
    #     return -1

    # def remove(self, key: int) -> None:
    #     hash_value = key % self.size

    #     for pair in self.buckets[hash_value]:
    #         if pair[0] == key:
    #             self.buckets[hash_value].remove(pair)

# You are given an array of integers nums, sort the array in ascending order and return it.

# You must solve the problem without using any built-in functions in O(nlog(n)) time complexity and with the smallest space complexity possible.

# Example 1:

# Input: nums = [10,9,1,1,1,2,3,1]

# Output: [1,1,1,1,2,3,9,10]
# Example 2:

# Input: nums = [5,10,2,1,3]

# Output: [1,2,3,5,10]
# Constraints:

# 1 <= nums.length <= 50,000.
# -50,000 <= nums[i] <= 50,000
class Heap_Sort:
    def sortArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        
        # phase 1: build max heap
        for index in range((n - 2) // 2, -1, -1):
            self.heapify(nums, index, n)

        # phase 2: repeat until sorted
        for end in range(n - 1, 0, -1):
            nums[0], nums[end] = nums[end], nums[0]

            self.heapify(nums, 0, end)
        return nums

    def heapify(self, nums: List[int], i: int, heap_size: int) -> None:
        while True:
            left = 2*i + 1
            right = 2*i + 2
            largest = i

            if left < heap_size and nums[left] > nums[largest]:
                largest = left
            if right < heap_size and nums[right] > nums[largest]:   
                largest = right
            
            if largest == i:
                return 
            
            nums[i], nums[largest] = nums[largest], nums[i]
            i = largest

# You are given an array nums consisting of n elements where each element is an integer representing a color:

# 0 represents red
# 1 represents white
# 2 represents blue
# Your task is to sort the array in-place such that elements of the same color are grouped together and arranged in the order: red (0), white (1), and then blue (2).

# You must not use any built-in sorting functions to solve this problem.

# Example 1:

# Input: nums = [1,0,1,2]

# Output: [0,1,1,2]
# Example 2:

# Input: nums = [2,1,0]

# Output: [0,1,2]
# Constraints:

# 1 <= nums.length <= 300.
# 0 <= nums[i] <= 2.

def countingSort(nums: List[int]) -> List[int]:
    # because we only have 3 numbers, we can use that to rewrite every element
    # in the array with a counter array
    counter = [0] * 3 # [0, 0, 0]
    for num in nums:
        counter[num] += 1 # use the value as index, and increment the value
    
    index = 0
    for i in range(len(counter)):
        while(counter[i]): # stop when counter[i] reaches 0
            nums[index] = i
            counter[i] -= 1
            index += 1

# Given an integer array nums and an integer k, return the k most frequent elements within the array.
# The test cases are generated such that the answer is always unique.
# You may return the output in any order.

# Example 1:
# Input: nums = [1,2,2,3,3,3], k = 2
# Output: [2,3]

# Example 2:
# Input: nums = [7,7], k = 1
# Output: [7]

# Constraints:
# 1 <= nums.length <= 10^4.
# -1000 <= nums[i] <= 1000
# 1 <= k <= number of distinct elements in nums.
def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    counter = {}
    for num in nums:
        counter[num] = counter.get(num, 0) + 1
    
    heap = []
    for num, freq in counter.items():
        heapq.heappush(heap, (freq, num))

        if len(heap) > k:
            heapq.heappop(heap)
    
    res = []
    for _ in range(k):
        res.append(heapq.heappop(heap)[1])
    return res
    
