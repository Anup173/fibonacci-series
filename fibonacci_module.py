# J. Pocahontas Olson  June 2016
# Module containing function definitions relating to the Fibonacci numbers

import math

# Golden ratio definitions
phi = (1+math.sqrt(5))/2
psi = (1-math.sqrt(5))/2


# A check to ensure that inputs are positive integers, which most of these functions require
def ensure_positive_int(num):
    # Make sure it's an integer
    try:
        val = int(num)
    except ValueError:
        raise ValueError("Could not interpret your input as an integer")
        return num
    
    # Make sure it's positive
    if (val < 0):
        raise ValueError(num, ' is not positive.')
    
    return val


# For a given integer n, print out the first n Fibonacci numbers
def fibList(num):
    try:
        num = ensure_positive_int(num)
    except ValueError:
        print("Please enter a positive integer for the number of Fibonacci numbers to generate.")
        return []
    
    fibNumbers = []
    
    if num >= 1:
        fibNumbers.append(0)
    if num >= 2:
        fibNumbers.append(1)
    if num > 2:  # assert: fibNumbers = [0, 1]
        i=2
        while i <= num-1:  # -1 adjusts for zero-indexing
            fibNumbers.append( fibNumbers[i-2] + fibNumbers[i-1] )
            i += 1
    if num < 0:
        raise ValueError('Invalid input. ', num, ' should be a positive integer.')
    
    return fibNumbers
