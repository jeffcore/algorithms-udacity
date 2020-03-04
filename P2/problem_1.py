"""
Finding the Square Root of an Integer
Find the square root of the integer without using any Python library. 
You have to find the floor value of the square root.

For example if the given number is 16, then the answer would be 4.

If the given number is 27, the answer would be 5 because sqrt(5) = 5.196 whose floor value is 5.

The expected time complexity is O(log(n))

Here is some boilerplate code and test cases to start with:
"""
import math
def sqrt(number):
   """
   Calculate the floored square root of a number

   Args:
      number(int): Number to find the floored squared root
   Returns:
      int: Floored Square Root
   """
   
   if number < 0:
       return None
   
   if number == 0 or number == 1 :      
      return number
   
   start_num = 1
   end_num = number

   while start_num <= end_num:
      mid = (start_num + end_num) // 2

      mid_sqr = mid * mid

      if mid_sqr == number:         
         return mid

      if mid_sqr < number:
         start_num = mid + 1
         ans = mid
      else:
         end_num = mid - 1
   
   return ans

print('Test Batch 1')
print ("Pass" if  (3 == sqrt(9)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (4 == sqrt(16)) else "Fail")
print ("Pass" if  (1 == sqrt(1)) else "Fail")
print ("Pass" if  (5 == sqrt(27)) else "Fail")


print('Test Batch 2')
print ("Pass" if  (5 == sqrt(25)) else "Fail")
print ("Pass" if  (0 == sqrt(0)) else "Fail")
print ("Pass" if  (15 == sqrt(225)) else "Fail")
print ("Pass" if  (35 == sqrt(1225)) else "Fail")

print('Test Batch 3')
print ("Pass" if  (15 == sqrt(238)) else "Fail")
print ("Pass" if  (92 == sqrt(8568)) else "Fail")
print ("Pass" if  (8 == sqrt(66)) else "Fail")
print ("Pass" if  (81 == sqrt(6561)) else "Fail")
print ("Pass" if  (None == sqrt(-25)) else "Fail")

# References:
# https://www.geeksforgeeks.org/find-square-root-number-upto-given-precision-using-binary-search/