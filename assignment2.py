# 1. Write a program that takes a number n and prints the first n numbers in the Fibonacci sequence. Use both Recursion and regular method

#regular method

number = int(input('Enter any number: '))
a,b = 0,1
for i in range(number):
    print(a, end = ",")
    a,b = b, a+b 


#using recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# Print first n Fibonacci numbers
num = int(input("Enter how many terms: "))
for i in range(num):
    print(fibonacci(i), end=", ")
