from typing import List
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
    validPalindrome,
    palindromNumberStringConversion,
    palindromeNumber,
    mergeLinkedLists,
    length_of_cycle,
    container_with_most_water,
    two_sum_ii
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
    print("validPalindrome: ", validPalindrome("apple"))

    print("palindromNumberStringConversion: ", palindromNumberStringConversion(-1))
    print("palindromNumberStringConversion: ", palindromNumberStringConversion(100))
    print("palindromNumberStringConversion: ", palindromNumberStringConversion(1001))
    print("palindromNumberStringConversion: ", palindromNumberStringConversion(1234321))

    print("palindromeNumber: ", palindromeNumber(1001))
    print("palindromeNumber: ", palindromeNumber(1234321))
    print("palindromeNumber: ", palindromeNumber(123456))
    print("palindromeNumber: ", palindromeNumber(3332333))
    
    nodes = build_linked_list_with_cycle()
    print("length of cycle: ", length_of_cycle(nodes))

    print("container with most water", container_with_most_water([2, 9, 6, 2, 5, 3, 5, 10, 1]))
    print("container with most water", container_with_most_water([1,1]))

    print("two sum 2: ", two_sum_ii([1, 2, 3, 4], 6))
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(values):
    dummy = ListNode(0)
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next

def build_linked_list_with_cycle() -> ListNode:
    nodes = [ListNode(i) for i in [1, 2, 3, 4, 5]]
    for i in range(len(nodes) - 1):
        print(i)
        nodes[i].next = nodes[i + 1]
    nodes[4].next = nodes[1]
    return nodes[0]

if __name__ == "__main__":
    run()