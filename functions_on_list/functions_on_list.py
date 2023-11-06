"""
@author: waziri
"""

from math import *
import sys

def isdigit(L):
    result = False
    
    for i in L:
        try:
           val = int(i)
           result = True
        except ValueError:
          try:
              val = float(i)
              result = True
          except ValueError:
              return False        
    return result


# 1. Function myLength(L) that, given a list, returns its length.
def myLength(L):
    print("-------------- ", sys._getframe().f_code.co_name," --------------")
    return len(L)


# 2. Function myMaximum(L) that, given a non-empty list, returns its maximum.
def myMaximum(L):
    print("-------------- ", sys._getframe().f_code.co_name," --------------")
    return max(L)


# 3. Function average(L) that, given a non-empty list of numbers, returns its average.   
def average(L):
    print("-------------- ", sys._getframe().f_code.co_name," --------------")
    if(len(L) > 0):
        return sum(L)/len(L) if (isdigit(L) == True) else None
     
    else:
        return None


# 4. Function buildPalindrome(L) that, given a list, returns the palindrome that
# starts with the reverse of the list.
def buildPalindrome(L):
    return

# 5. Function remove(L1, L2) that, given a list L1 and a list L2, returns the list L1
# after removing the occurrences of the elements in L2.
def remove(L1, L2):
    print("-------------- ", sys._getframe().f_code.co_name," --------------")                   
    return [i for i in L1 if i not in L2]


# 6. Function flatten(L) that recursively flattens a list whose elements may also
# be lists of different levels. Hint: use recursion and the isinstance(x, list) built-in
# function.
def flatten(L):
    print("-------------- ", sys._getframe().f_code.co_name," --------------")
    flattened_list = []
    for i in L:
        if(isinstance(i, list) == True):
            flatten(i)
        else:
            flattened_list.append(i)
    
    return flattened_list


# 7. Function oddsNevens(L) that, given a list of integers, returns two lists, one
# with all the odd numbers and one with all the even numbers, in the same relative
# order than the original.
def oddsNevens(L):
    print("-------------- ", sys._getframe().f_code.co_name," --------------")
    odd_list = []
    even_list = []
    for i in L:
        if (i % 2) == 0:
            even_list.append(i)
        else:
            odd_list.append(i)
    return odd_list, even_list


# 8. Function primeDivisors(n) that returns the list of all prime divisors of a non-
# zero positive integer.
def primeDivisors(n):
    print("-------------- ", sys._getframe().f_code.co_name," --------------")
    prime_divisor = []
    
    if n > 0:
        while n % 2 == 0: 
           prime_divisor.append(2)
           n = n / 2
        
        for i in range(3, int(sqrt(n))+1, 2): 
            while n % i == 0: 
                prime_divisor.append(i) 
                n = n / i
        
        if n > 2: 
            prime_divisor.append(n)
        
    return prime_divisor


# 9. Function is_increasing(L) that returns a list of booleans. A number is
# increasing if every digit is less than or equal to the digit which is on its right (if
# any).
def is_increasing(L):
    print("-------------- ", sys._getframe().f_code.co_name," --------------")
    bool_is_increasing = []
    counter = 1
    for i in L:
        if(counter < len(L)):
            if(i <= L[counter]):
                bool_is_increasing.append(True)
            else:
                bool_is_increasing.append(False)
            
            counter = counter + 1
        else:
            bool_is_increasing.append(False)
            
    return bool_is_increasing
        


# my_list_test = [2,4,8,5,6]
# my_list_test_1 = [8,6,7,2]

# removeL1 = [2,2,4,8,5,6]
# removeL2 = [8,5,1,3,9,2]
# list_to_flatten = [[2,4,8,5,6], 4, [8,6,7,2], [2,2,4,8,5,6], 5]

# print(myLength(my_list_test), "\n")
# print(myMaximum(my_list_test), "\n")
# print(average(my_list_test), "\n")
# print(is_increasing(my_list_test), "\n")
# print(primeDivisors(500), "\n")
# print(oddsNevens(my_list_test), "\n")
# print(remove(removeL1, removeL2), "\n")
# print(flatten(list_to_flatten), "\n")
