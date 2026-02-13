from collections import defaultdict, Counter
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