# J. Pocahontas Olson   June 2016
# Fibonacci generator

import fibonacci_module as fb

print ("First 5: ", fb.fibList(5))
print ("First 100: ", fb.fibList(100))

print ("Error Testing")
print ("  n=0: ",fb.fibList(0))
print ("  n=1: ",fb.fibList(1))
print ("  n=2: ",fb.fibList(2))
print ("  n=3.2: ",fb.fibList(3.2))
print ("  n=3.6: ",fb.fibList(3.9))
print ("  n=-1: ",fb.fibList(-1))
print ("  n=foo: ",fb.fibList("foo"))