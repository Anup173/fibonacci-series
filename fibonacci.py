# J. Pocahontas Olson   June 2016
# Fibonacci generator

# For a given integer n, print out the first n Fibonacci numbers
def fib(num):
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

print ("First 5: ", fib(5))
print ("First 100: ", fib(100))

print ("Error Testing")
print ("  n=0: ",fib(0))
print ("  n=1: ",fib(1))
print ("  n=2: ",fib(2))
print ("  n=3.2: ",fib(3.2))
print ("  n=3.6: ",fib(3.9))
print ("  n=-1: ",fib(-1))
print ("  n=foo: ",fib("foo"))