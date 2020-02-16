### Find Files Recursive ###
import os
def find_files(suffix, path):
    """
    Find all files beneath path with file name suffix.

    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.

    There are no limit to the depth of the subdirectories can be.

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """
    results = []
    start_path = "./" + path
    if os.path.isdir(path):
        results = find_files_recursive(suffix, start_path)

    return results

def find_files_recursive(suffix, path):    
    result = []
    path_items = os.listdir(path)   
    for item in path_items:     
        item_path = path + '/' + item  
        if os.path.isdir(item_path):            
            result = result + find_files_recursive(suffix, item_path)
        elif os.path.isfile(item_path):
            if item_path.endswith(suffix):
                result.append(item_path)    
                       
    return result

# print(find_files('.h','testdir'))

# Test 1 - Correct Solution
solution = ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']
assert(find_files('.c','testdir') == solution), 'Did not work - Correct Solution'

# Test 2 - Incorrect Start Directory
solution = []
assert(find_files('.c','testdir_wrong') == solution), 'Did not work - Incorrect Start Directory'

# Test 3 - Find Different File Extension .h
solution = ['./testdir/subdir3/subsubdir1/b.h', './testdir/subdir5/a.h', './testdir/t1.h', './testdir/subdir1/a.h']
assert(find_files('.h','testdir') == solution), 'Did not work - Find Different File Extension .h'

# Let us print the files in the directory in which you are running this script
# print('test')
# print (os.listdir("./testdir"))

# # Let us check if this file is indeed a file!
# print (os.path.isfile("./ex.py"))

# # Does the file end with .py?
# print ("./ex.py".endswith(".py"))