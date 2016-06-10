# Fibonacci numbers, for EMC / Virtustream tech screen.  
# J Pocahontas Olson   June 2016
This directory contains a machine learning investigation of Fibonacci numbers, written in python.
Future plans include making a simple resting web app for Fibonacci numbers, written in python and flask.

###################################
####     MACHINE LEARNING      ####
###################################

To run machine learning part:
    At a command line on a terminal, enter:
            python fibonacci.py

This executes a python script that investigates machine learning, using the Fibonacci numbers
as input data to fit.  
It graphs the data, obtains a fit to predict Fibonacci numbers, and evaluates it against the true calculated
Fibonacci numbers.  
Then, because a theorectical limit exists, we try that as well.

Finally, we artificially create a "noisey" input of Fibonacci numbers



To test machine learning part:
    At a command line on a terminal, enter:
            python test_script.py

This has tests for invalid inputs to the fibonacci number calculator, and some of the 
theoretical predictions.



###################################
####          WEB APP          ####
###################################
To run web app:
At a command line on a terminal, enter:
        ./run.py

This starts the webservice on your local computer.  
Open the domain in your browser, with port 5000: http://localhost:5000/

The start page will bring you to the fibonacci calculator section, http://localhost:5000/fib/,
which displays usage.
To display the first n fibonacci numbers, enter that value after the slash:
    http://localhost:5000/fib/<num>  where <num> is the number of Fibonacci numbers to output.
Output is truncated after 10,000 digits.  Scientific notation is acceptable.