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

def fibonacci (number): # defining fibonacci function with parameter
    fibo = [0,1]        # creating two first elements of fibo list
    i = 2               # starting at the 3rd number in Fibonacci sequence
    while i <= number:  # loop; checking the iteration count
        fibo.append(fibo[i-1]+fibo[i-2])  # computing & adding new fibonacci numbers to already created fibo list
        i = i + 1       # incrementing iteration count
    return fibo[number] # returning result


user_input = input("Enter the n-th number of Fibonacci sequence you would like to learn") # user input; no validation
print fibonacci(user_input) # printing result


