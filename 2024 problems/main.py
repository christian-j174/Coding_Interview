
"""
Why?
Execution Plan?
"""

"""
Solutions:
From Hardest to Easiest:

1. Using Gaus Sum, then restarle la suma esperada con la obtenida.
2. Some N x N iteration, but the constraint is the time complexity. 
3. A simple iteration that add each number to an hashmap or dictionary. 

"""


#Problem 3 April 19, 2024
def find_missing_number(arr):
    """Using Gauss Sum to find the missing number in the array."""
    gaus_sum = len(arr) * (len(arr) + 1) // 2
    total_sum = sum(arr)
    return gaus_sum - total_sum
    






#Problem 1
"""
Write a function get_middle_char(s) that takes a string
s as input and returns the middle character(s) of the string,
or an empty string if the length of the input string is even.
"""

def get_middle_char(s):
    string_size = len(s)
    if(string_size == 0 or (string_size % 2 == 0)):
        return ""
    else:
        middle_position = string_size // 2
        return s[middle_position]


#Problem 2
""" 
Write a function that receives two numbers as input snd returns the bigger
amoung the two. 

"""
def max(n1, n2):
    if n1 > n2:
        return n1
    else:
        return n2




#Problem 4
"""Write a function named sum that gets a number n
 and returns the sum of the numbers from 1 to n. """

#Iteractive Solution 
def sum(n):
    total = 0
    for i in range(1, n+1):
        total += i
    
    return total


# Recursive solution
def sum(n):
    if n == 0:
        return 0
    else:
        return sum(n-1) + n 



#Reverse a string
def reverse(s):
    output = ""
    size = len(s) -1

    while(size >= 0):
        output += s[size]
        size = size - 1

    return output








def main():
    find_missing_number([1, 0, 3, 4, 2])
    return 0



if __name__ == "__main__":
    main()
