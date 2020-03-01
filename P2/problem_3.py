"""
Rearrange Array Elements
Rearrange Array Elements so as to form two number such that their sum is 
maximum. Return these two numbers. You can assume that all array elements 
are in the range [0, 9]. The number of digits in both the numbers cannot 
differ by more than 1. You're not allowed to use any sorting function that 
Python provides and the expected time complexity is O(nlog(n)).

for e.g. [1, 2, 3, 4, 5]

The expected answer would be [531, 42]. Another expected answer can be [542, 31]. In 
scenarios such as these when there are more than one possible answers, return any one.

Here is some boilerplate code and test cases to start with:
"""

# merge sort 
# add odd to first number
# add even to second number


def mergesort(items):
    if len(items) <= 1:
        return items
    
    mid = len(items) // 2
    left = items[:mid]
    right = items[mid:]
    
    left = mergesort(left)
    right = mergesort(right)
    
    return merge(left, right)
    
def merge(left, right):    
    merged = []
    left_index = 0
    right_index = 0
    
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(right[right_index])
            right_index += 1
        else:
            merged.append(left[left_index])
            left_index += 1

    merged += left[left_index:]
    merged += right[right_index:]
        
    return merged



def rearrange_digits(input_list):
    """
    Rearrange Array Elements so as to form two number such that their sum is maximum.

    Args:
       input_list(list): Input List
    Returns:
       (int),(int): Two maximum sums
    """
    sorted_list = mergesort(input_list)
    
    num_one = 0
    num_two = 0
    for i in range(len(sorted_list)):
        if (i % 2 == 0): 
            num_two = num_two * 10 + sorted_list[i] 
        else:             
            num_one = num_one * 10 + sorted_list[i] 
    print(f'number 1 : {num_one} number 2: {num_two}')

    return num_one, num_two


def test_function(test_case):
    output = rearrange_digits(test_case[0])
    solution = test_case[1]
    if sum(output) == sum(solution):
        print("Pass")
    else:
        print("Fail")

test_function([[1, 2, 3, 4, 5], [542, 31]])
test_function([[4, 6, 2, 5, 9, 8], [964, 852]])
