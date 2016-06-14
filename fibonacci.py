# J. Pocahontas Olson   June 2016
# Fibonacci generator

import fibonacci_module as fb         # Custom module made for this project
import math                           # Math functions (log, pow, sqrt, etc.)
import matplotlib.pyplot as plt       # Plotting
plt.style.use('ggplot')
import pylab
from scipy.optimize import curve_fit  # Curve fitting


BIGNUM = 100
# Let's investigate!  Graph first BIGNUM Fibonacci numbers
y = fb.fibList(BIGNUM)
x = list(range(BIGNUM))
plt.figure(1)
plt.plot(x, y)
plt.xlabel('n^th Fibonacci number')
plt.ylabel('Fibonacci number')
plt.title('First ' + str(BIGNUM) + ' Fibonacci numbers')
print("..Made graph of first", BIGNUM, "Fibonacci numbers..")
#plt.yscale('log')  # Uncomment to see log graph
## => Clearly exponential growth

## Let's try to fit the data!
# Instead of fitting exponential growth, we'll fit a line to the log of the
#   fibonacci numbers, which is better than fitting exponential for large n.
def fitLogPrediction(x, m, b):    # (Log scale)
    return m * x + b
log_x = x[1:]  # Ignore first fibonacci number b/c log(0) is undefined
log_y = [math.log(fibNum) for fibNum in y[1:]]
# Convert fit of log scale to actual predictor of fibonacci number (rounds to nearest int)
def fitFibPrediction(x, m, b):
    return round(math.exp(fitLogPrediction(x, m, b)))

# Fit the line and plot it in red
popt, pcov = curve_fit(fitLogPrediction, log_x, log_y)   # Finds slope and y-intercept that best fit
fit_y = [fitLogPrediction(x_index,popt[0],popt[1]) for x_index in log_x]  # Makes line that fits
plt.figure(2)
plt.plot(log_x, log_y, "bs")  # Log values in blue squares
plt.plot(log_x, fit_y, 'r-')  # Fit in red dashes
plt.xlabel('n^th Fibonacci number')
plt.ylabel('Log of Fibonacci number')
plt.title('Log of Fibonacci numbers and their fit')
print("..Made graph of Log of Fibonacci numbers and their fit..")

## Not too shabby, let's see how that fit performs
# For large n, the slope approaches phi = (1+sqrt(5))/2.  Let's see what we got.
print("Compare the fitted line's slope: ", math.exp(popt[0]))
print("        to the golden ratio phi: ", fb.phi)
print("Using only", BIGNUM, "Fibonacci numbers, the fit's slope differs from")
print("        the theoretical limit by", 100*(1- math.exp(popt[0])/fb.phi), "%")


# Let's see how well our fit did
fit_differences = [y[x_index] - fitFibPrediction(x_index,popt[0],popt[1]) for x_index in x]
plt.figure(3)
plt.subplot(211)
plt.plot(x, fit_differences)
plt.xlabel('n^th Fibonacci number')
plt.ylabel('Difference')
plt.title('Difference from true Fibonacci number and fit')
fit_percent_differences = [(y[x_index] - fitFibPrediction(x_index,popt[0],popt[1]))/y[x_index] for x_index in x[1:]]
plt.subplot(212)
plt.plot(x[1:], fit_percent_differences)
plt.xlabel('n^th Fibonacci number')
plt.ylabel('Percent Difference')
plt.title('Percent Difference from true Fibonacci number and fit')
print("..Made graphs of difference, and percent difference, from true Fibonacci number and fit..")


## Pretty good fit we came up with.  Let's see how the theoretical limit performs.
#    (Added Binet's formula definitions to the Fibonacci module, and tests to test_script.py)
binet_differences = [y[x_index] - fb.f_Binet(x_index) for x_index in x]
plt.figure(4)
plt.subplot(211)
plt.plot(x, binet_differences)
plt.xlabel('n^th Fibonacci number')
plt.ylabel('Difference')
plt.title('Difference from true Fibonacci number and theoretical prediction')
binet_percent_differences = [(y[x_index] - fb.f_Binet(x_index))/y[x_index] for x_index in x[1:]]
plt.subplot(212)
plt.plot(x[1:], binet_percent_differences)
plt.xlabel('n^th Fibonacci number')
plt.ylabel('Percent Difference')
plt.title('Percent Difference from true Fibonacci number and theoretical prediction')
print("..Made graphs of difference, and percent difference, from true Fibonacci number and theoretical prediction..")

## Which is better?



# Show graphs that we made
pylab.show()





####   Can we clean up noisy data?   ####
## Let's suppose we're measuring something that should be Fibonacci numbers,
## but there's some noise in the measurement.
## Given that we know we should be getting Fibonacci numbers,
## can we remove the noise?
## I've written an API to mimic this data collection, called noisy_input_API.py

import noisy_input_API as api
