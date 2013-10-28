"""
The MIT License (MIT)

Copyright (c) 2013 Pawel Kalinowski

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.

"""

# Recursive method to compute n-th Fibonacci number

def fibonacci (number): # defining fibonacci function with parameter

    if number == 0:  # base case no. 1
        return 0
    if number == 1:  # base case no. 2
        return 1
    else:
        return fibonacci(number-2)+fibonacci(number-1) # recursive method which is based on two base cases

user_input = input("Enter n-th number of Fibonacci sequence you would like to learn") # enter input; no validation

fibonacci_of_user_input = fibonacci(user_input) # feeding user input to fibonacci function
print fibonacci_of_user_input # print result
