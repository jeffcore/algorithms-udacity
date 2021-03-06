"""
Search in a Rotated Sorted Array
You are given a sorted array which is rotated at some random pivot point.

Example: [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]

You are given a target value to search. If found in the array return its index, 
otherwise return -1.

You can assume there are no duplicates in the array and your algorithm's 
runtime complexity must be in the order of O(log n).

Example:

Input: nums = [4,5,6,7,0,1,2], target = 0, Output: 4

Here is some boilerplate code and test cases to start with:

"""

def rotated_array_search(input_list, number):
    """
    Find the index by searching in a rotated sorted array

    Args:
       input_list(array), number(int): Input array to search and the target
    Returns:
       int: Index or -1
    """
    result = binary_search(input_list, number, 0, len(input_list)-1)
    # print('result' , result)
    return result

def binary_search(alist, item, low, high):
    """Your code goes here."""
   
    while low <= high:
        if len(alist) == 0 :
            return -1        
        else:
            midpoint = (high + low)//2
          
            if alist[midpoint] == item:
                return midpoint
            
            if alist[midpoint] < alist[high]:
                # right half is sorted
                if alist[midpoint] < item <= alist[high]:
                    low = midpoint + 1
                else:
                    high = midpoint - 1
            else:
                if alist[low] <= item < alist[midpoint]:
                    high = midpoint - 1
                else:
                    low = midpoint + 1

    return -1

def linear_search(input_list, number):
    for index, element in enumerate(input_list):
        if element == number:
            return index
    return -1

def test_function(test_case):
    input_list = test_case[0]
    number = test_case[1]
    # print('linear num ', linear_search(input_list, number))
    if linear_search(input_list, number) == rotated_array_search(input_list, number):
        print("Pass")
    else:
        print("Fail")

test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 6])
test_function([[6, 7, 8, 9, 10, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 8])
test_function([[6, 7, 8, 1, 2, 3, 4], 1])
test_function([[6, 7, 8, 1, 2, 3, 4], 10])


test_function([[6], 6])
test_function([[6], 10])
test_function([[10, 1, 2, 3, 4], 10])
test_function([[10, 1, 2, 3, 4], 1])
test_function([[10, 1, 2, 3, 4], 2])
test_function([[10, 1, 2, 3, 4], 3])
test_function([[10, 1, 2, 3, 4], 4])
test_function([[10, 1, 2, 3, 4], 5])