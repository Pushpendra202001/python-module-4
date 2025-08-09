# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
# 2.   Returns the calculated factorial.
# 3.   Calls the function with a sample number and prints the output
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)
try:
    num = int(input("Enter a number: "))
except ValueError:
    print("please enter a number")
else:
    result = factorial(num)
    print("factorial of", num, "is:", result)
