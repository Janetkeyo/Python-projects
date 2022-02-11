import math

def isPerfectSquare(num):
    # finding the square root of num
    s =int(math.sqrt(num))
    return s*s == num
 
def isFibonacciNumber(n):
    # return true if the number is fibonacci otherwise
    # return false
    return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4)
 
 
n = int(input("Enter the number you want to check : "))
if(isFibonacciNumber(n) == True):
    print(n  ," is a fibonacci number")
else:
    print(n  ," is not a fibonacci number")