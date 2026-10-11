# =============================================================================
# Performance Lab
# Run this file directly (python performance_lab.py) to execute all tests.
# =============================================================================


# 🔍 Problem 1: Find Most Frequent Element
# Given a list of integers, return the value that appears most frequently.
# If there's a tie, return any of the most frequent.
#
# Example:
# Input: [1, 3, 2, 3, 4, 1, 3]
# Output: 3

def most_frequent(numbers):
    """Return the most frequent value, or None for an empty list."""
    if not numbers:
        return None

    counts = {}              
    best_value = None
    best_count = 0

    for value in numbers:
        counts[value] = counts.get(value, 0) + 1
        if counts[value] > best_count:       
            best_count = counts[value]
            best_value = value

    return best_value

"""
Time and Space Analysis for problem 1:
- Best-case: O(n). We still check every element.
- Worst-case: O(n). One pass, and dictionary lookups are O(1).
- Average-case: O(n).
- Space complexity: O(n) in the worst case, because the dictionary stores each different value.
- Why this approach? A dictionary counts each value in one pass. Counting with numbers.count() for every value would be O(n^2).
- Could it be optimized? Not really. We have to look at every element, so O(n) is the best possible.
- Trade-offs: It uses extra memory to save time. Sorting first would use less
  memory but take more time.
"""


def test_most_frequent():
    assert most_frequent([1, 3, 2, 3, 4, 1, 3]) == 3        
    assert most_frequent([]) is None                         
    assert most_frequent([7]) == 7                            
    assert most_frequent([5, 5, 5, 5]) == 5                   
    assert most_frequent([-1, -1, 2, 2, -1]) == -1           
    assert most_frequent([0, 0, 1]) == 0                     
    assert most_frequent([1, 2, 3, 1, 2, 3]) in {1, 2, 3}    
    assert most_frequent([1, 2, 2, 1]) in {1, 2}            
    big = list(range(1000)) + [42] * 5
    assert most_frequent(big) == 42                          
    print("Problem 1: all tests passed")


# 🔍 Problem 2: Remove Duplicates While Preserving Order
# Write a function that returns a list with duplicates removed but preserves order.
#
# Example:
# Input: [4, 5, 4, 6, 5, 7]
# Output: [4, 5, 6, 7]

def remove_duplicates(nums):
    """Return a new list with duplicates removed, keeping first occurrences."""
    seen = set()
    result = []
    for n in nums:
        if n not in seen:        
            seen.add(n)
            result.append(n)
    return result

"""
Time and Space Analysis for problem 2:
- Best-case: O(n). We look at every item once.
- Worst-case: O(n). Checking a set is fast, so each item takes about the same
  small amount of time.
- Average-case: O(n).
- Space complexity: O(n). If no items repeat, the set and the new list both
  hold every item.
- Why this approach? The set remembers what we have already seen, so we can
  check quickly. The list keeps the items in order. Checking the list each
  time instead would be much slower, O(n^2).
- Could it be optimized? Not really. We have to look at every item, so O(n)
  is the best possible. list(dict.fromkeys(nums)) is shorter code, but it is
  the same speed.
- Trade-offs: It uses extra memory to save time.
"""


def test_remove_duplicates():
    assert remove_duplicates([4, 5, 4, 6, 5, 7]) == [4, 5, 6, 7]   # example
    assert remove_duplicates([]) == []                              # empty
    assert remove_duplicates([1]) == [1]                            # single
    assert remove_duplicates([2, 2, 2, 2]) == [2]                   # all same
    assert remove_duplicates([1, 2, 3]) == [1, 2, 3]                # no dups
    assert remove_duplicates([3, 1, 3, 2, 1]) == [3, 1, 2]          # order kept
    assert remove_duplicates([-1, 0, -1, 0]) == [-1, 0]             # neg/zero
    original = [1, 1, 2]
    remove_duplicates(original)
    assert original == [1, 1, 2]                                    # no mutation
    assert remove_duplicates(list(range(1000)) * 3) == list(range(1000))
    print("Problem 2: all tests passed")


# 🔍 Problem 3: Return All Pairs That Sum to Target
# Write a function that returns all unique pairs of numbers in the list that sum to a target.
# Order of output does not matter. Assume input list has no duplicates.
#
# Example:
# Input: ([1, 2, 3, 4], target=5)
# Output: [(1, 4), (2, 3)]

def find_pairs_original(nums, target):
    """ORIGINAL (brute-force) version, kept for comparison with find_pairs."""
    pairs = []
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):          
            if nums[i] + nums[j] == target:
                pairs.append((min(nums[i], nums[j]), max(nums[i], nums[j])))
    return pairs


def find_pairs(nums, target):
    """
    IMPROVED VERSION.

    HOW I OPTIMIZED: My first version used two loops to check every possible pair. This version loops through the list once and keeps a set of the numbers it has seen. The trade-off is that it uses extra memory for the set.
    """
    seen = set()
    pairs = []
    for x in nums:
        complement = target - x
        if complement in seen:
            pairs.append((min(x, complement), max(x, complement)))
        seen.add(x)
    return pairs

"""
Time and Space Analysis for problem 3 (the improved version, find_pairs):
- Best-case: O(n). We still look at every number once.
- Worst-case: O(n). Checking a set is fast, so each number takes about the same amount of time.
- Average-case: O(n).
- Space complexity: O(n). The set holds the numbers we have seen, and the list holds the pairs we found.
- Why this approach?  A set answers if a number has been seen quickly.
- Could it be optimized? No. We have to look at every number, so O(n) is the best.
- Trade-offs:
    -Two loops is slow, but uses less memory.
    - The set is faster but uses extra memory.

Speed comparison (first version vs. improved version, tested on my computer):
    n = 1,000   : first ~ 14.3 ms   | improved ~ 0.11 ms
    n = 5,000   : first ~ 365.0 ms   | improved ~ 0.60 ms
    n = 10,000  : first ~ 1,452.0 ms  | improved ~ 1.20 ms
The first version gets about 4 times slower when the list size doubles. The improved version only gets 2 times slower.
Memory: the improved version uses a set, which is a small price for the speed.
"""


def test_find_pairs():
    def normalize(pairs):
        return sorted(tuple(sorted(p)) for p in pairs)

    for fn in (find_pairs, find_pairs_original):
        assert normalize(fn([1, 2, 3, 4], 5)) == [(1, 4), (2, 3)]      
        assert fn([], 5) == []                                          
        assert fn([3], 3) == []                                         
        assert fn([1, 2, 3], 100) == []                                 
        assert normalize(fn([2, 4], 6)) == [(2, 4)]                     
        assert fn([2, 5, 7], 4) == []                                   
        assert normalize(fn([-3, -1, 0, 1, 3], 0)) == [(-3, 3), (-1, 1)]  
        assert normalize(fn([0, 5], 5)) == [(0, 5)]                     
        assert normalize(fn([1, 2, 3, 4, 5, 6], 7)) == [(1, 6), (2, 5), (3, 4)]
    data = list(range(-500, 500))
    assert normalize(find_pairs(data, 10)) == normalize(find_pairs_original(data, 10))
    print("Problem 3: all tests passed")


# 🔍 Problem 4: Simulate List Resizing (Amortized Cost)
# Create a function that adds n elements to a list that has a fixed initial capacity.
# When the list reaches capacity, simulate doubling its size by creating a new list
# and copying all values over (simulate this with print statements).
#
# Example:
# add_n_items(6) → should print when resizing happens.

def add_n_items(n, initial_capacity=4, verbose=True):
    
    capacity = initial_capacity
    storage = [None] * capacity         
    size = 0
    total_copies = 0                    

    for item in range(n):
        if size == capacity:             
            new_capacity = capacity * 2
            new_storage = [None] * new_capacity
            for i in range(size):        
                new_storage[i] = storage[i]
            total_copies += size
            if verbose:
                print(f"Resizing: capacity {capacity} -> {new_capacity} "
                      f"(copied {size} items)")
            storage, capacity = new_storage, new_capacity
        storage[size] = item
        size += 1

    return size, capacity, total_copies

"""
Time and Space Analysis for problem 4:
- When do resizes happen? When the list is full and we try to add one more
  item. If we start with room for 4 items, a resize happens when we add the
  5th item, then the 9th, then the 17th, and so on.
- What is the worst-case for a single append? O(n). The append that causes a
  resize has to copy every item to the new list.
- What is the amortized time per append overall? O(1). Resizes are rare, and
  the total copying over n appends adds up to less than 2n. Spread out, that
  is only a few steps per append.
- Space complexity: O(n). The list is never much bigger than twice the number
  of items in it.
- Why does doubling reduce the cost overall? After each resize, there is
  plenty of empty room, so the next many appends are quick. The big copy
  happens less and less often. If we only added a few spots each time, we
  would have to copy over and over, which would be much slower.
"""


def test_add_n_items():
    import io
    from contextlib import redirect_stdout

    # n = 0: nothing added, no resize
    assert add_n_items(0, verbose=False) == (0, 4, 0)
    assert add_n_items(3, verbose=False) == (3, 4, 0)
    assert add_n_items(4, verbose=False) == (4, 4, 0)
    assert add_n_items(5, verbose=False) == (5, 8, 4)
    assert add_n_items(6, verbose=False) == (6, 8, 4)
    assert add_n_items(9, verbose=False) == (9, 16, 12)
    assert add_n_items(5, initial_capacity=1, verbose=False) == (5, 8, 1 + 2 + 4)

   
    
    with redirect_stdout(buf):
        add_n_items(3)
    assert buf.getvalue() == ""
    buf = io.StringIO()
    with redirect_stdout(buf):
        add_n_items(6)
    assert buf.getvalue().count("Resizing") == 1


    for n in (10, 100, 1000, 100000):
        size, cap, copies = add_n_items(n, verbose=False)
        assert size == n and cap >= n and copies < 2 * n
    print("Problem 4: all tests passed")


# 🔍 Problem 5: Compute Running Totals
# Write a function that takes a list of numbers and returns a new list
# where each element is the sum of all elements up to that index.
#
# Example:
# Input: [1, 2, 3, 4]
# Output: [1, 3, 6, 10]
# Because: [1, 1+2, 1+2+3, 1+2+3+4]

def running_total(nums):
    """Return a new list where result[i] == sum(nums[:i+1])."""
    result = []
    total = 0
    for n in nums:
        total += n              
        result.append(total)
    return result

"""
Time and Space Analysis for problem 5:
- Best-case: O(n). We look at every number once.
- Worst-case: O(n). For each number, we do one addition and one append.
- Average-case: O(n).
- Space complexity: O(n). The new list holds one total for every number.
- Why this approach? Each running total is the last total plus the current number, so we just keep one running sum. 
- Could it be optimized? Not really. We have to look at every number, so O(n)
  is the best possible.
- Trade-offs: Making a new list keeps the original list safe, but uses extra memory. Changing the original list would save memory, but we would lose data.
"""


def test_running_total():
    assert running_total([1, 2, 3, 4]) == [1, 3, 6, 10]           # example
    assert running_total([]) == []                                 # empty
    assert running_total([5]) == [5]                               # single
    assert running_total([0, 0, 0]) == [0, 0, 0]                   # zeros
    assert running_total([-1, -2, -3]) == [-1, -3, -6]             # negatives
    assert running_total([5, -5, 5, -5]) == [5, 0, 5, 0]           # sign flips
    assert running_total([1.5, 2.5]) == [1.5, 4.0]                 # floats
    original = [1, 2, 3]
    running_total(original)
    assert original == [1, 2, 3]                                   # no mutation
    big = list(range(1, 10001))
    assert running_total(big)[-1] == 10000 * 10001 // 2            # large input
    print("Problem 5: all tests passed")


# =============================================================================
# Run everything
# =============================================================================
if __name__ == "__main__":
    test_most_frequent()
    test_remove_duplicates()
    test_find_pairs()
    test_add_n_items()
    test_running_total()
    print("\nAll tests passed!")
