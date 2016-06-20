# J. Pocahontas Olson   June 2016
# Fibonacci generator

import fibonacci_module as fb         # Custom module made for this project
import math                           # Math functions (log, pow, sqrt, etc.)
import matplotlib.pyplot as plt       # Plotting
plt.style.use('ggplot')
import pylab
from scipy.optimize import curve_fit  # Curve fitting
from sklearn.metrics import mean_squared_error  # Error of fit
from distutils.util import strtobool  # Translates user answer to Yes/No question to bool

FIRSTPOINTS  = int(100)
PREDICTPOINT = int(500)

# Introduction to user
print("Welcome!")

###############################
### (1.)  Graph first 100 (FIRSTPOINTS) Fibonacci numbers
###############################
y = fb.fibList(FIRSTPOINTS)
x = list(range(1,FIRSTPOINTS+1))  # Adjusts for index starting at 0
print("Would you like to see a graph of the first", FIRSTPOINTS, "Fibonacci numbers? ")
showit = strtobool(input("  [Figure 1]  Y/N: "))
if showit:
    plt.figure(1)
    plt.plot(x, y)
    plt.xlabel('n^th Fibonacci number')
    plt.ylabel('Fibonacci number')
    plt.title('First ' + str(FIRSTPOINTS) + ' Fibonacci numbers')
    #plt.yscale('log')  # Uncomment to see log graph
    pylab.show(block=False)
print("\nFrom Figure 1, we can see that the Fibonnaci numbers grow exponentially.")


##############################
## (2.) Let's try to fit the data!
##############################
print("Our first thought would be to fit an exponential to this data.")
print("However, because of the large numbers involved, it's better to fit")
print("a line to the log of the Fibonacci numbers.")
# Generate the log values of the true Fibonacci numbers
log_x = x[1:]  # Ignore first fibonacci number b/c log(0) is undefined
log_y = [math.log(fibNum) for fibNum in y[1:]]
# Define a line to fit the log of the Fib numbers
def fitLogPrediction(x, m, b):    # x is input, and m and b are the slope and y-intercept of the line, respectively
    return m * x + b
# Function to convert from the fit of log scale, to actual prediction of fibonacci number (rounds to nearest int)
def fitFibPrediction(x, m, b):
    return round(math.exp(fitLogPrediction(x, m, b)))
# Find 500th (PREDICTPOINT) Fibonacci number as well
predictList = fb.fibList(PREDICTPOINT)

# Fit the line, plot it in red, predict 500th point
popt, pcov = curve_fit(fitLogPrediction, log_x, log_y)   # Finds slope and y-intercept that best fit
fit_y = [fitLogPrediction(nFib,popt[0],popt[1]) for nFib in log_x]  # Makes the line that fits
fitlog500prediction = fitLogPrediction(PREDICTPOINT,popt[0],popt[1])
actual500num = predictList[PREDICTPOINT-1]
# Find error bars for extrapolated predictions
logerror = math.sqrt(mean_squared_error(log_y, fit_y))*math.sqrt(FIRSTPOINTS)
lower500bound = math.exp(fitlog500prediction-logerror)
upper500bound = math.exp(fitlog500prediction+logerror)
print("\nFitting a line to the data, the best fit has slope\n", popt[0], "and y-intercept", popt[1])

# For large n, the slope approaches phi = (1+sqrt(5))/2.  Let's see what we got.
print("We can compare this to the theoretical limit (applicable for large n),\n  which should yield the golden ratio.")
print("Compare the fit's prediction: ", math.exp(popt[0]))
print("     to the golden ratio phi: ", fb.phi)
print("\nSo after using only", FIRSTPOINTS, "Fibonacci numbers, the fit behavior differs from")
print("     the theoretical limit by", 100*(1- math.exp(popt[0])/fb.phi), "%")

print("\nWould you like to see a graph of the line we fit to the \nfirst", FIRSTPOINTS,
      "Fibonacci numbers, on a log scale? ")
showit = strtobool(input("  [Figure 2]  Y/N: "))
if showit:
    plt.figure(2)
    plt.subplot(211)
    plt.plot(log_x, log_y, "bs")  # Log values in blue squares
    plt.plot(log_x, fit_y, 'r-')  # Fit in red dashes
    plt.xlabel('n^th Fibonacci number')
    plt.ylabel('Log of Fibonacci number')
    plt.title('Fitted prediction of Fibonacci numbers, on log scale')
    plt.subplots_adjust(hspace=0.5)
    plt.subplot(212)
    plt.plot(log_x + [PREDICTPOINT], log_y + [math.log(actual500num)], "bs")  # Log values in blue squares
    plt.plot(log_x + [PREDICTPOINT], fit_y + [fitlog500prediction], 'r-')  # Fit in red dashes
    plt.xlabel('n^th Fibonacci number')
    plt.ylabel('Log of Fibonacci number')
    plt.title('Same graph, extrapolated to predict 500th Fibonacci number')
    pylab.show(block=False)
print("From Figure 2, we can see that the fit seems to match the first", int(FIRSTPOINTS),"Fibonacci numbers well,")
print("and extrapolating the fit to predict the", int(PREDICTPOINT),"th Fibonacci number seems pretty good also.")
print("\nIn fact, the fit predicts the{0:4d}th Fibonacci number to be {1:12E},".format(int(PREDICTPOINT), math.exp(fitlog500prediction)))
print("  within [{0:12E}, {1:12E}]. \nThe actual value, {2:12E}, is within these bounds.".format( lower500bound, upper500bound, actual500num))

print("\nNow let us investigate how much the fit is off by.")




#############################
# (3.) Let's see how well our fit did
#############################
fit_differences = [y[nFib-1] - fitFibPrediction(nFib-1,popt[0],popt[1]) for nFib in log_x]
fit_percent_differences = [(y[nFib-1] - fitFibPrediction(nFib-1,popt[0],popt[1]))/y[nFib-1] for nFib in log_x]

print("We have calculated the fit's prediction of the first", FIRSTPOINTS, "Fibonacci numbers,")
print("to compare to the actual Fibonacci numbers.")

## Differences from actual Fibonacci numbers
print("\nWould you like to see graphs of the differences, and percent differences,")
print("between the fit's prediction and the actual Fibonacci number?")
showit = strtobool(input("  [Figure 3]  Y/N: "))
if showit:
    plt.figure(3)
    plt.subplot(211)
    plt.plot(log_x, fit_differences)
    plt.xlabel('n^th Fibonacci number')
    plt.ylabel('Difference')
    plt.title('Difference from true Fibonacci number and fit')
    plt.ticklabel_format(style='sci', axis='y', scilimits=(-2,10))  # Sets scientific notation for axes
    plt.subplots_adjust(hspace=0.5)
    plt.subplot(212)
    plt.plot(log_x, fit_percent_differences)
    plt.xlabel('n^th Fibonacci number')
    plt.ylabel('Percent Difference')
    plt.title('Percent Difference from true Fibonacci number and fit')
    pylab.show(block=False)
print("From Figure 3, we can see that the prediction reproduces the Fibonacci numbers")
print("fairly well, but is off from the true value by more at large n.")
print("This is to be somewhat expected because of the expontentially increasing numbers involved.")
print("If you look at the percent differences, the prediction is within a hundreth of a percent.\n")


## Binet's prediction and its differences from actual Fibonacci numbers
print("The Fibonacci numbers have been well studied, and there is a closed-form expression")
print("to get the n^th Fibonacci number that uses the golden ratio.")
print("It's called Binet's formula, and more info's on wikipedia:")
print("   https://en.wikipedia.org/wiki/Fibonacci_number#Closed-form_expression")

print("\nBinet's formula is meant for large n (where the ratio of Fibonacci numbers is ")
print("closer to the golden ratio), but let's see what it predicts for the first 100 values.")

binet_differences = [y[nFib-1] - fb.f_Binet(nFib-1) for nFib in log_x]
binet_percent_differences = [(y[nFib-1] - fb.f_Binet(nFib-1))/y[nFib-1] for nFib in log_x]
print("\nWould you like to see the same graphs as before (differences and percent differences),")
print("but using Binet's formula to predict the n^th Fibonacci number instead of the fit we made?")
showit = strtobool(input("  [Figure 4]  Y/N: "))
if showit:
    plt.figure(4)
    plt.subplot(211)
    plt.plot(log_x, binet_differences)
    plt.xlabel('n^th Fibonacci number')
    plt.ylabel('Difference')
    plt.title('Difference from true Fibonacci number and theoretical prediction')
    plt.subplots_adjust(hspace=0.5)
    plt.subplot(212)
    plt.plot(log_x, binet_percent_differences)
    plt.xlabel('n^th Fibonacci number')
    plt.ylabel('Percent Difference')
    plt.title('Percent Difference from true Fibonacci number and theoretical prediction')
    pylab.show(block=False)
print("From Figure 4, we can see that Binet's prediction does better at large n.")
print("Our fit is limited by only being able to look at the first", FIRSTPOINTS, "Fibonacci numbers.")
print("Binet's formula is better at large n.  If I were to implement this, I would probably use")
print("the theoretical limit (Binet's formula) after a certain cut-off point (maybe around 20).")
print("Also, getting more data for our initial fit (for example, the first 10,000 Fibonacci numbers)")
print("would improve the accuracy of our fit.")




##############################
## (4.) Clean up noisy data
##############################
HIGHEST_FIB_N      = int(1000)
NUMBEROFDATAPOINTS = int(200)

print("\n\nWe now move on to part 5, simulating some data collection process, which")
print("obtains", NUMBEROFDATAPOINTS, "Fibonacci numbers with some Gaussian noise introduced.")
print("It's pulling initial values from the first", HIGHEST_FIB_N, "Fibonacci numbers.")

## Import API that generates noisy data
import noisy_input_API as api
import random

## Generate true Fibonacci numbers (between 1 and HIGHEST_FIB), to compare to predictions
fibs = fb.fibList(HIGHEST_FIB_N)
x = [random.randint(1, HIGHEST_FIB_N) for i in range(NUMBEROFDATAPOINTS)]
y = [fibs[x[i]-1] for i in range(NUMBEROFDATAPOINTS)]  #minus 1 adjusts for index starting at zero

## Generate noisy data
y_noise = api.add_noise(y)  # fib numbers with noise
noise_differences = [y_noise[i]-y[i] for i in range(NUMBEROFDATAPOINTS)]
noise_percent_differences = [(noise_differences[i]/y[i] if y[i]>0 else 0) for i in range(NUMBEROFDATAPOINTS)]

## Plot of noise
print("\nWould you like to see a plot of the noise we added to the Fibonacci numbers?")
showit = strtobool(input("  [Figure 5]  Y/N: "))
if showit:
    plt.figure(5)
    plt.plot(x, noise_percent_differences, marker='o',color='b',linestyle="None")
    plt.hlines(0, 0, HIGHEST_FIB_N, colors='r')
    pylab.xlim([1,HIGHEST_FIB_N])
    plt.xlabel('n^th Fibonacci number')
    plt.ylabel('Percent difference (signal-true)/true')
    plt.title('Noise from simulated measurer of Fibonacci number')
    pylab.show(block=False)
print("From Figure 5, we can see that the noise is fairly random.")
print("Since we are looking at percent differences, the size of the noise increases at")
print("higher n, to mimic the difficulty in being precise when large numbers are involved.")


## Clean-up noise
print("\nWe clean-up the data, by nudging the noisy value to the nearest Fibonacci number.")
print("We can not use the theoretical prediction (Binet's formula), unfortunately, because")
print("the numbers get too big too fast.")
print("Instead, I've implemented a way to save off a large amount of Fibonacci numbers to a binary file.")
print("This trades space for computational time later.")
print("I've also written a function to extract the nth Fibonacci number from that file")
print("without having to go the whole way through the file or load it entirely to memory.")
# Prompt to make a new saved file
import os.path
import distutils.util
if not os.path.isfile(fb.filename):
    ans = input("That saved file does not already exist. \n  Would you like to create one?: (Y/N) ")
    makenew = distutils.util.strtobool(ans)
    if makenew:
        make_saved_Fibonacci_file()
    else:
        print("Can't show you the cool 'nudging' function until you create the saved file.  Exiting now.")
        quit()

# Correct the noisy inputs
corrected_fib_numbers = [fb.nearest_saved_fib(y_noise[eachPoint]) for eachPoint in range(NUMBEROFDATAPOINTS)]
wrongPrediction = []
for value in range(NUMBEROFDATAPOINTS):
    if corrected_fib_numbers[value] != y[value]:
        wrongPrediction.append(value)
cleaned_differences = [corrected_fib_numbers[i]-y[i] for i in range(NUMBEROFDATAPOINTS)]

## Plot of error in clean-up
print("\nWhen cleaning up the data, we were wrong",len(wrongPrediction),"out of", NUMBEROFDATAPOINTS, "times.")
#print("\nWould you like to see a plot of how often we were wrong in cleaning up the data?")
#showit = strtobool(input("  [Figure 6]  Y/N: "))
#if showit:
#    plt.figure(6)
#    plt.hist([abs(number) for number in cleaned_differences], bins = range(0,NUMBEROFDATAPOINTS,1))
#    plt.xlabel('How much we were wrong by')
#    plt.ylabel('How often we were wrong by this much')
#    plt.title('Error in cleaning up noisy data')
#    pylab.show(block=False)
print("Would you like to see when we got the wrong number?")
showit = strtobool(input("  [Table 1]  Y/N: "))
if showit:
    print("   Orig n     Orig Fib num     Noisey input     Corrected Fib")
    for wrong in wrongPrediction:
        print('{:11d}  {:11E} {:16E} {:16E}'.format(x[wrong], y[wrong], y_noise[wrong],corrected_fib_numbers[wrong]))
print("From Table 1, we see that we were only wrong when")
print("the noise was so big that it passed the nearest Fibonacci number.")




##############################
##           END            ##
##############################
print("\n\nThis concludes our run-though of using machine learning to predict Fibonacci numbers.")
print("Thank you, and enjoy your day!")
pylab.show()
