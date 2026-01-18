from hash_map import (
    twoSum,
    singleNumberHashMap,
    containsDuplicate,
    containsDuplicateHashMap,
    happyNumber,
    groupAnagrams,
    groupAnagramsAlphabetMap,
    groupAnagramsSort,
    longestPalindrome,
    missingNumber
)
from two_pointers import (
    validPalindrome
)


def run():
    # Hashmap
    print(twoSum([2,7,11,15], 9))          # [0,1]
    print(twoSum([3,2,4], 6))              # [1,2]

    print(singleNumberHashMap([2,2,1]))
    print(singleNumberHashMap([4,2,1,2,1]))
    
    print(containsDuplicate([1,2,3,4,5]))
    print(containsDuplicateHashMap([4,2,1,3,2]))

    print(happyNumber(19))

    print(groupAnagrams(["ate", "tea", "nat", "apple", "tan", "leppa"]))
    print(groupAnagramsAlphabetMap(["ate", "tea", "nat", "apple", "tan", "leppa"]))
    print(groupAnagramsSort(["ate", "tea", "nat", "apple", "tan", "leppa"]))

    print(longestPalindrome("apuils"))

    print(missingNumber([0,1]))
    print(missingNumber([3, 0, 1]))
    print(missingNumber([9,6,4,2,3,5,7,0,1]))

    print("Hasmap tests finished ✓")

    # two pointers
    print(validPalindrome("apple"))




if __name__ == "__main__":
    run()