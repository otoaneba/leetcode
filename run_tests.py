from hash_map import twoSum
from hash_map import (
    singleNumberHashMap,
    containsDuplicate,
    containsDuplicateHashMap,
    happyNumber,
    groupAnagrams,
    groupAnagramsAlphabetMap,
    groupAnagramsSort,
    longestPalindrome
)

def run():
    # Two Sum
    print(twoSum([2,7,11,15], 9))          # [0,1]
    print(twoSum([3,2,4], 6))              # [1,2]

    print("All tests finished ✓")

    print(singleNumberHashMap([2,2,1]))
    print(singleNumberHashMap([4,2,1,2,1]))
    
    print(containsDuplicate([1,2,3,4,5]))
    print(containsDuplicateHashMap([4,2,1,3,2]))

    print(happyNumber(19))

    print(groupAnagrams(["ate", "tea", "nat", "apple", "tan", "leppa"]))
    print(groupAnagramsAlphabetMap(["ate", "tea", "nat", "apple", "tan", "leppa"]))
    print(groupAnagramsSort(["ate", "tea", "nat", "apple", "tan", "leppa"]))

    print(longestPalindrome("apuils"))


if __name__ == "__main__":
    run()