from hash_map import twoSum
from hash_map import singleNumberHashMap
# from two_pointers import ...
# from dp import ...

def run():
    # Two Sum
    print(twoSum([2,7,11,15], 9))          # [0,1]
    print(twoSum([3,2,4], 6))              # [1,2]

    print("All tests finished ✓")

    print(singleNumberHashMap([2,2,1]))
    print(singleNumberHashMap([4,2,1,2,1]))

if __name__ == "__main__":
    run()