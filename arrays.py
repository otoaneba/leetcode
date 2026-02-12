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