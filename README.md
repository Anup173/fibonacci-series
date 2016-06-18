# Fibonacci numbers, for EMC / Virtustream tech screen.  
# J Pocahontas Olson   June 2016
This directory contains a machine learning investigation of Fibonacci numbers, written in python.
There is also a simple resting web app for Fibonacci numbers, written in Python with Flask.

This github repository is the code submission for the tech screen for Virtustream.  My task is slightly modified, as I am applying for a data scientist role.  My assignment was to "do something with machine learning that involves the Fibonacci numbers".  I did that, and the regular tech screen too, because I thought it would be fun.  
The Machine Learning section of the README below describes my interpretation of "machine learning with Fibonacci numbers", and the problem I invented to solve.


###################################
####           SET-UP          ####
###################################

Clone this github repository to your machine, and ensure you have python version 3 or above installed, 
and Flask (sudo pip3 install flask).
The machine learning part also uses the matplotlib & scipy modules, which you will have to install (python -m pip install <module name>) if you haven't already.



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



###################################
####     MACHINE LEARNING      ####
###################################
##  Task  ##
To mimic the format of the web app requirements, I made my own definition for what all should be in the machine learning code screen.
# -------------------------------------------------- #
Please provide a sample project for review:
1.  The project should calculate and plot the first 100 Fibonacci numbers.
2.  Determine a method to predict the 500th Fibonacci number, using only the first 100 numbers.
3.  Describe the accuracy rate of your prediction, and make any relevant comparisons to other predicitons.
4.  Suppose we are measuring something that we know should yield Fibonacci numbers, like bumps on tree trunks, a bunny population, a visual scan of arrangement of sunflower seeds, etc.  Real world measurements won't produce the Fibonacci numbers exactly, but with some noise.  
    Write an API to simulate noisey fibonacci numbers, and plot it.
    Write a function that will remove the noise, by replacing the value with the nearest located Fibonacci number.
5. Include some functional tests for all code you write
6. Use any language that you know well


##  Code  ##
I've written a python script that walks the user through the thought-process and displays the plots.
To run it, at a command line on a terminal, enter:
    python fibonacci.py

I've also included tests for all the functions written.  As it is intentionally trying to cause errors,
I've put all the terminal calls within a try/catch.
To run the tests, at a command line on a terminal, enter:
    python test_script.py
