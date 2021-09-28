#maximumoftwonumbersusing function
'''def maximumOfNumbers(a, b):
    if a > b :
        return a
    else:
        return b

a = int(input("Enter the first number a : "))
b = int(input("Enter the second number b : "))
print(maximumOfNumbers(a, b))'''

def maxOfNumbers():
    if (a > b > c):
        return a
    elif (b > a > c):
        return b 
    else:
        return c
a = int(input("Enter a : "))
b = int(input("Enter b : "))
c = int(input("Enter c : "))
print(maxOfNumbers())
