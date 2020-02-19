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
    """
    recursive call to locate directories and iterate over 
    files in each directory

    Args:
      suffix(str): suffix if the file name to be found
      path(str): path of the file system

    Returns:
       a list of paths
    """   
    if suffix == "":
        return []
    
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

def test_results(solution, test):
    if solution.sort() == test.sort():
        return True
    else:
        return  False

# Test 1 - Correct Solution
print('Test 1 - Correct Solution')
solution = ['./testdir/subdir3/subsubdir1/b.c', './testdir/t1.c', './testdir/subdir5/a.c', './testdir/subdir1/a.c']
print(f'solution is: {solution} \n result: {find_files(".c","testdir")}')
assert(test_results(solution, find_files('.c','testdir'))== True), 'Did not work - Correct Solution'

# Test 2 - Incorrect Start Directory
print('Test 2 - Incorrect Start Directory')
solution = []
print(f'solution is: {solution} result: {find_files(".c","testdir_wrong")}')
assert(find_files('.c','testdir_wrong') == solution), 'Did not work - Incorrect Start Directory'

# Test 3 - Empty suffix
print('Test 3 - Empty suffix')
solution = []
print(f'solution is: {solution}  result: {find_files("","testdir")}')
assert(solution == find_files("","testdir")), 'Did not work - Find Different File Extension .h'
