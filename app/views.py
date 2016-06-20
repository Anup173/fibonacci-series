from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title="Home")

@app.route('/test_script.html')
def test_script():
    return render_template('test_script.html')

@app.route('/fib/')
def fib_usage():
    return render_template('usage.html')

@app.route('/fib/<string:argument>')
def myFib(argument):
    TRUNCATE_AFTER_THIS_MANY = 1e4
    
    # Validate input
    try:
        number = int(float(argument))  # Float handles scientific notation
    except:
        message = "Could not interpret " + argument + " as an integer.  Please enter a positive integer in the url."
        return render_template('usage.html', msg = message)
    if number < 0:
        message = "Invalid input. " + str(number) + " must be a positive integer. Please try again."
        return render_template('usage.html', msg = message)
    
    def fibList(num):
        fibNumbers = []
        message = ""
            
        if num >= 1:
            fibNumbers.append(0)
        if num >= 2:
            fibNumbers.append(1)
        if num > 2:  # assert: fibNumbers = [0, 1]
            if num > TRUNCATE_AFTER_THIS_MANY:
                num = TRUNCATE_AFTER_THIS_MANY
                message = "Truncated output after " + str(int(TRUNCATE_AFTER_THIS_MANY)) + " numbers."
            i=2
            while i <= num-1:  # -1 adjusts for zero-indexing
                fibNumbers.append( fibNumbers[i-2] + fibNumbers[i-1] )
                i += 1
        if num < 0:
            message = "Invalid input. " + str(num) + " should be a positive integer."
            raise ValueError(message)

        return (fibNumbers, message)


    #return 'First %d Fibonacci numbers: %s' % (number, fibList(number))
    fibs = fibList(number)
    return render_template('output.html', num=number, list=fibs[0], msg = fibs[1])
