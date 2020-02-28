"""
Max and Min in a Unsorted Array
In this problem, we will look for smallest and largest 
integer from a list of unsorted integers. The code should 
run in O(n) time. Do not use Python's inbuilt functions to find min and max.

Bonus Challenge: Is it possible to find the max and min in a single traversal?
"""
def get_min_max(ints):
    """
    Return a tuple(min, max) out of list of unsorted integers.

    Args:
       ints(list): list of integers containing one or more integers
    """
    if len(ints) == 0:
        return None, None

    if len(ints) == 1:
        return ints[0], ints[0]

    min_num = float('inf')
    max_num = float('-inf')

    for i in ints:
        if i < min_num:
            min_num = i
        if i > max_num:
            max_num = i
    
    return min_num, max_num


## Example Test Case of Ten Integers
import random

# Test 1 - Basic tests
l = [i for i in range(0, 10)]  # a list containing 0 - 9
random.shuffle(l)
print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")

l = [2,3,45,6,4,3,2,2]  # a list containing 0 - 9
print ("Pass" if ((2,45) == get_min_max(l)) else "Fail")

# Test 2: edge cases
l = [1]  # a list containing 0 - 9
print ("Pass" if ((1,1) == get_min_max(l)) else "Fail")
l = []  # a list containing 0 - 9
print ("Pass" if ((None,None) == get_min_max(l)) else "Fail")

# Test 3: Ultimate Random Tests
import random
passed = True
number_of_tests = 10000
print(f'{number_of_tests} Random Test Cases Are Running')
for _ in range(number_of_tests):
    len_list = random.randrange(2,2000)
    l = []
    for _ in range(len_list):
        l.append(random.randrange(0,5000))

    min_num = min(l)
    max_num = max(l)
    if not ((min_num, max_num) == get_min_max(l)):
        print(f'Fail - {l} min {min_num} max {max_num}')
        passed = False

if passed:
    print(f"All {number_of_tests} random tests Passed")